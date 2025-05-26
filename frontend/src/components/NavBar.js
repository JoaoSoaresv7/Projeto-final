/*
Aprendizados:
React: biblioteca base que permite criar componentes.
useState: hook usado para criar e controlar estado (abre/fecha o menu lateral)
hook: função especial que o React fornece para usar funcionalidades internas do React em componentes funcionais.
Drawer: é um painel lateral deslizante
*/

import React, { useState } from "react";
import logo from "../assets/logo.png"; //Importa a imagem do logotipo da pizzaria
import { BsCart2 } from "react-icons/bs"; //Importa o ícone de carrinho de compras da biblioteca react-icons
import HomeIcon from "@mui/icons-material/Home"; // ícones do Material UI Icons
import InfoIcon from "@mui/icons-material/Info";// ícones do Material UI Icons
import PhoneRoundedIcon from "@mui/icons-material/PhoneRounded"; // ícones do Material UI Icons
import ShoppingCartRoundedIcon from "@mui/icons-material/ShoppingCartRounded"; // ícones do Material UI Icons
import { HiOutlineBars3 } from "react-icons/hi2"; //Ícone de menu hambúrguer do pacote Heroicons (hi2)
import Drawer from "@mui/material/Drawer";//Cria um painel lateral deslizante (Drawer)
import Box from "@mui/material/Box";// Componente auxiliar de layout do Material UI
import List from "@mui/material/List"; //Todos fazem parte da construção da lista de opções dentro do menu lateral 
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

const NavBar = () => {
  /*Hook do react*/
  const [openMenu, setOpenMenu] = useState(false);
  const menuOptions = [
    {
      text: "Home",
      icon: <HomeIcon />,
    },
    {
      text: "Sobre Nós",
      icon: <InfoIcon />,
    },
    {
      text: "Contato",
      icon: <PhoneRoundedIcon />,
    },
    {
      text: "Carrinho",
      icon: <ShoppingCartRoundedIcon />,
    },
  ];
  return (
    <nav>
      <div className="nav-logo-container">
        <img src={logo} alt="logo"></img>
      </div>

      <div className="navbr-links-container">
        <a href="#home">Home</a>
        <a href="#sobre">Sobre Nós</a>
        <a href="#contato">Contato</a>
        <a href="#contato">
          <BsCart2 className="navbar-cart-icon" />
        </a>

        <button className="primary-button">Reservas Agora</button>
      </div>

      <div className="nav-bar-menu-container">
        <HiOutlineBars3 onClick={() => setOpenMenu(true) /*Abre*/} />
      </div>

      <Drawer
        open={openMenu}
        onClose={() /*Fecha*/ => setOpenMenu(false)}
        anchor="right"
      >
        <Box
          sx={{ width: 250 }}
          role="presentation"
          onClick={() => setOpenMenu(false)}
          onKeyDown={() => setOpenMenu(false)}
        >
          <List>
            {menuOptions.map((item) => (
              <ListItem key={item.text} disablePadding>
                <ListItemButton>
                  <ListItemIcon>{item.icon}</ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
    </nav>
  );
};
export default NavBar;
