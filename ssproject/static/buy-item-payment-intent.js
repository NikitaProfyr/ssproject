// Получение токена CSRF из формы
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

fetch('/get-key/')
    .then(res => res.json())
    .then(data =>  {
        const stripe = Stripe(data.key)
        // Создаем экземпляр объекта Elements
        const elements = stripe.elements();

        // Создаем элементы ввода для данных карты
        const cardNumber = elements.create('cardNumber');
        cardNumber.mount('#card-number');

        const cardExpiry = elements.create('cardExpiry');
        cardExpiry.mount('#card-expiry');

        const cardCvc = elements.create('cardCvc');
        cardCvc.mount('#card-cvc');
        const idItem = document.getElementById('id-item').innerHTML

        document.getElementById('payment-form').addEventListener('submit', async (event) => {
            event.preventDefault();

            // Получаем данные карты
            const {paymentMethod, error} = await stripe.createPaymentMethod({
                type: 'card', card: cardNumber, billing_details: {
                    name: document.getElementById('card-name').value
                }
            });
            if (error) {
                // Ошибка обработки платежа
                alert(error.message)
            } else {
                // Отправляем данные о платеже на сервер для обработки
                fetch(`/buy/${idItem}`, {
                    method: 'POST', headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    }, body: JSON.stringify({paymentMethod: paymentMethod.id}),
                })
                    .then(response => response.json())
                    .then(data => {
                        // console.log(data)
                        window.location.href = '/success-payment/'
                    }).catch(e => {
                        alert(e)
                        console.log(e)
                        window.location.href = '/failed-payment/'
                });
            }
        });
    })



