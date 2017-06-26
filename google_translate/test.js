const translate = require('google-translate-api');

// translate('A small brown dog wearing a white shirt on top of a skateboard.', {from: 'en', to: 'ko'}).then(res => {
//     console.log(res.text);
//     console.log(res.from.text.autoCorrected);
//     console.log(res.from.text.value);
//     console.log(res.from.text.didYouMean);
// }).catch(err => {
//     console.error(err);
// });


translate('I speak Dutch!', {from: 'en', to: 'ko'}).then(res => {
    console.log(res.text);
}).catch(err => {
    console.error(err);
});