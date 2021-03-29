#!/bin/bash
# Author: Zeta
git clone https://github.com/zeta-sys/instv2rayzeta.git
chmod 777 instv2rayzeta/instalador.sh
echo -e "\e[1;41mINSTALANDO  "V2RAY BY ZETA" ESPERE POR FAVOR......\e[1;m"
./instv2rayzeta/instalador.sh
sudo rm -rf instv2rayzeta  
while true; do
    read -p "¿DESEAS INSTALAR BADVPN (Necesario para juegos/videollamadas)? ESCRIBA YES o NO..."   yn
    case $yn in
        [Yy]* ) wget https://raw.githubusercontent.com/rockz5555/badvpn-installer/master/badvpn-installer.sh && bash badvpn-installer.sh; break;;
        [Nn]* ) echo -e "\e[1;41mELIGIO NO INSTALAR BADVPN, SI DESEA INSTALAR, REINSTALE SCRIPT......\e[1;m";exit;;
        * ) echo -e "\e[1;41mPOR FAVOR INGRESAR "YES" O "NO"......\e[1;m";;
    esac
done
echo -e "\e[1;44mINSTALACION COMPLETADA......\e[1;m"
echo -e "\e[1;44mINGRESE "V2RAY" PARA UTILIZAR EL PANEL ADMINISTRADOR......\e[1;m"
