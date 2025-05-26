import AboutBackground from "../assets/pizza2.png";
import AboutBackgroundImage from "../assets/pizza.jpg";
import { BsFillPlayCircleFill } from "react-icons/bs";

const About = () => {
  return (
    <div className="about-section-container">
      <div className="about-background-image-container">
        <img src={AboutBackground} alt="Imagem da pizza" />
      </div>

      <div className="about-section-image-container">
        <img src={AboutBackgroundImage} alt="Mão segurando pizza" />
      </div>

      <div className="about-section-text-container">
        <p className="primary-subheading">Sobre Nós</p>
        <h1 className="primary-heading">
          É Importante Conhecer Quem Alimenta Você
        </h1>

        <p className="primary-text">
          Somos uma pizzaria universitária dedicada a trazer a você as pizzas
          mais deliciosas do DF
        </p>

        <p className="primary-text">
          Nossa história começou com um projeto da matéria de Estrutura de
          Dados, com o desejo de criar um trabalho inovador e util
        </p>

        <div className="about-buttons-container">
          <button className="secondary-button">Leia Mais</button>
          <button className="watch-video-button">
            <BsFillPlayCircleFill /> Assista Nosso Vídeo
          </button>
        </div>
      </div>
    </div>
  );
};

export default About;
