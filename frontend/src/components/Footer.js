import { BsLinkedin, BsTwitterX, BsYoutube } from "react-icons/bs";
import Logo from "../assets/logo.png";
import { FiFacebook } from "react-icons/fi";

const Footer = () => {
  return (
    <div className="footer-wrapper">
      <div className="footer-section-one">
        <div className="footer-logo-container">
          <img src={Logo} alt="Logo" />
        </div>
        <div className="footer-icons">
          <BsTwitterX />
          <BsLinkedin />
          <BsYoutube />
          <FiFacebook />
        </div>
      </div>

      <div className="footer-section-two">
        <div className="footer-section-columns">
          <span>Qualidade</span>
          <span>Ajuda</span>
          <span>Nossa Marca</span>
        </div>

        <div className="footer-section-columns">
          <span>61 99816-4471</span>
          <span>dev.gabrielimalmeida@gmail.com</span>
          <span>gabrielimalmeida@gmail.com</span>
        </div>

        <div className="footer-section-columns">
          <span>Termos & Condições</span>
          <span>Politica de Privacidade</span>
        </div>
      </div>
    </div>
  );
};

export default Footer;
