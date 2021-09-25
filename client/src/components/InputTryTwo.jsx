import axios from 'axios'

function InputTryTwo() {
  const sendData = () => {

    var crypto = require('crypto');
    var assert = require('assert');

    var algorithm = 'aes256'; // or any other algorithm supported by OpenSSL
    var key = '00000000000000000000000000000000';
    var iv = '0000000000000000';
    var text = 'hello world';

    var cipher = crypto.createCipheriv(algorithm, key, iv);
    var encrypted = cipher.update(text, 'utf8', 'hex') + cipher.final('hex');
    console.log('encrypted', encrypted, encrypted.length)

    axios.get('http://localhost:4444/user-info', {
      params: { user_string: encrypted }
    })
      .then(res => {
        console.log(res)
      })
  }
  return (
    <div>
      <button onClick={sendData}>click me</button>
    </div>
  )
}

export default InputTryTwo
