let stripe;

fetch('/get-key/')
    .then(res => res.json())
    .then(data => {
        stripe = Stripe(data.key)
        // const stripe = Stripe(apikey)
        // // Создаем экземпляр объекта Elements
        // const elements = stripe.elements();
        //
        // // Создаем элементы ввода для данных карты
        // const cardNumber = elements.create('cardNumber');
        // cardNumber.mount('#card-number');
        //
        // const cardExpiry = elements.create('cardExpiry');
        // cardExpiry.mount('#card-expiry');
        //
        // const cardCvc = elements.create('cardCvc');
        // cardCvc.mount('#card-cvc');
        // const idOrder = document.getElementById('id-order').innerHTML
        //
        // document.getElementById('payment-form').addEventListener('submit', async (event) => {
        //   event.preventDefault();
        //
        //   // Получаем данные карты
        //   const { paymentMethod, error } = await stripe.createPaymentMethod({
        //     type: 'card',
        //     card: cardNumber,
        //     billing_details: {
        //       name: document.getElementById('card-name').value
        //     }
        //   });
        //
        //   if (error) {
        //     // Ошибка обработки платежа
        //     console.error(error);
        //   } else {
        //     // Отправляем данные о платеже на сервер для обработки
        //     fetch(`/buy/order/${idOrder}`, {
        //       method: 'POST',
        //       headers: {
        //         'Content-Type': 'application/json',
        //       },
        //       body: JSON.stringify({ paymentMethod: paymentMethod.id }),
        //     })
        //     .then(response => response.json())
        //     .then(data => {
        //       console.log(data)
        //       if (data.success) {
        //         // Платеж успешен
        //         console.log('Платеж успешен');
        //       } else {
        //         // Обработка платежа не удалась
        //         console.error('Ошибка обработки платежа');
        //       }
        //     });
        //   }
        // });
    })


const buyOrder = (idOrder) => {

    fetch(`/buy/order/${idOrder}`)
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            return stripe.redirectToCheckout({sessionId: data.session})
        })
        .then((res) => {
            console.log(res);
        })


}

const button = document.getElementById('button-buy')
const idOrder = document.getElementById('id-order').innerHTML

button.addEventListener("click", () => buyOrder(idOrder))