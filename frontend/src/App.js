import './App.css';
import  Home from './Home';
import { Main } from './Main';
import { Navbar } from './Navbar';
import Login from './pages/Login';
import Signup from './pages/Signup';
import {BrowserRouter,Routes,Route} from "react-router-dom"


function App() {
  return (
<BrowserRouter>
<Navbar/>
<Main/>
<Routes>
  <Route path="/signup" element={<Signup/>}/>
  <Route path='/login' element={<Login/>}/>
  <Route path="/home" element={<Home/>}/>
  <Route path="/" element={<Main/>}/>
  
</Routes>

</BrowserRouter>
  );
}

export default App;
