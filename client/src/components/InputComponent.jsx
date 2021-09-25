import React, { useState } from 'react';
import axios from 'axios'
const crypto = require('crypto');

function InputComponent() {
  const [typed, setTyped] = useState("")
  const [encryptedState, setEncryptedState] = useState("")
  const [returnedData, setReturnedData] = useState("")
  const sendData = () => {

    let password = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';

    let encrypt = function (input, password) {
        var m = crypto.createHash('md5');
        m.update(password)
        var key = m.digest('hex');

        m = crypto.createHash('md5');
        m.update(password + key)
        var iv = m.digest('hex');

        var data = new Buffer(input, 'utf8').toString('binary');

        var cipher = crypto.createCipheriv('aes-256-cbc', key, iv.slice(0,16));

        // UPDATE: crypto changed in v0.10
        // https://github.com/joyent/node/wiki/Api-changes-between-v0.8-and-v0.10
        //var nodev = process.version.match(/^v(\d+)\.(\d+)/);
        var encrypted;
        encrypted = cipher.update(data, 'binary') + cipher.final('binary');

        /*if( nodev[1] === '0' && parseInt(nodev[2]) < 10) {
            encrypted = cipher.update(data, 'binary') + cipher.final('binary');
        } else {
            encrypted = cipher.update(data, 'utf8', 'binary') + cipher.final('binary');
        }*/

        var encoded = new Buffer(encrypted, 'binary').toString('base64');

        return encoded
    };

    let encoded = encrypt(typed, password)
    setEncryptedState(encoded)

    axios.get('http://localhost:4444/user-info', {
      params: { user_string: encoded }
    })
      .then(res => {
        setReturnedData(res.data)
      })
  }
  return (
    <div>
      <input onChange={(event) => setTyped(event.target.value)}></input>
      <button onClick={sendData}>click me</button>
      <div>What you entered: {typed}</div>
      <div>What you sent: {encryptedState}</div>
      <div>What was returned: {returnedData}</div>
    </div>
  )
}

export default InputComponent
