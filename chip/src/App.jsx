import './App.css'
import ChipList from './Chiplist'


function App() {

  const sampleChips = [
    { label: "123456" },
    { label: "1234567" },
    { label: "12345678" },
    { label: "12345" },
    { label: "123456789" }
  ];
  
  return (
    <div>
      <h1>Chips</h1>
      <ChipList chips={sampleChips} maxChipsDisplayed={3} maxTextLength={6} />
    </div>
  )
}

export default App
