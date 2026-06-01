import './App.css';
import Main  from './Main';
import Login from './Components/Login/Login';
import Signup from './Components/Signup/Signup';
import {BrowserRouter,Routes,Route} from "react-router-dom"
import  ProductList  from './pages/ProductList/ProductList';
import Navbar from './Components/Navbar/Navbar';
import { Product } from './pages/Product/Product';
import { WishlistPage } from './pages/WishlistPage/WishlistPage';
import Cart from './pages/Cart/Cart';
import Profile from './pages/Profile/Profile';
import Footer from './Components/Footer/Footer';


function App() {
  return (
<BrowserRouter>
<Navbar/>
<Routes>
  <Route path="/signup" element={<Signup/>}/>
  <Route path='/login' element={<Login/>}/>
  <Route path="/" element={<Main/>}/>
  <Route path='/productlist/:id' element={<ProductList/>}/>
  <Route path='/product/:id' element={<Product/>}/>
  <Route path="/:category"   element={<Main/>} />
  <Route path="/wishlist" element={<WishlistPage/>}/>
  <Route path='/cart' element={<Cart/>}/>
  <Route path='/profile' element={<Profile/>}/>
</Routes>

</BrowserRouter>
  );
}

export default App;
