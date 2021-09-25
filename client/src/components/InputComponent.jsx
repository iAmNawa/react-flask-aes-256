import axios from 'axios'

function InputComponent() {
  const sendData = () => {
    axios.get('http://localhost:4444/user-info')
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

export default InputComponent
