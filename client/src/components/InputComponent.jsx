import axios from 'axios'

function InputComponent() {
  const sendData = () => {
    console.log(axios)
  }
  return (
    <div>
      <button onClick={sendData}>click me</button>
    </div>
  )
}

export default InputComponent
