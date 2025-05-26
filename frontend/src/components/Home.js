import NavBar from "./NavBar";
import BannerBackground from "../assets/home-banner-BannerBackground.png";
import pizza2 from "../assets/pizza2.png";
import { FiArrowRight } from "react-icons/fi";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="home-container">
      <NavBar />

      <div className="home-banner-container">
        <div className="home-bannerImage-container">
          <img src={BannerBackground} alt="imagem de fundo do home container" />
        </div>
        <div className="home-text-section">
          <h1 className="primary-heading">
            Sua pizza favorita Entregue em Sua Casa.
          </h1>
          <p className="primary-text">
            Diversos Sabores deliciosos para alegrar os seus melhores momentos.
            Peça já a sua e receba um mimo surpresa.
          </p>

          <Link to="/cliente">
            <button className="secondary-button">
              Faça seu pedido <FiArrowRight />
            </button>
          </Link>

          <p className="primary-text">
            Ou venha comer conosco em um ambiente climatizado e aconchegante com
            várias opções para seu pedido
          </p>
        </div>

        <div className="home-image-section">
          <div className="home-primary-image">
            <img src={pizza2} alt="pizza2" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
