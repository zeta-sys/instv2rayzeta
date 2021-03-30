#!/bin/bash
# Author: Zeta
echo -e "\e[1;44mPARA INSTALAR DEBE SER USUARIO ROOT - VERIFICANDO......\e[1;m"    
sleep 3                                                                        
if [ "$EUID" = 0 ]                                                                   
  then git clone https://github.com/zeta-sys/instv2rayzeta.git
  chmod 777 instv2rayzeta/instalador.sh
echo -e "\e[1;41mUSUSRIO ROOT DETECTADO - INSTALANDO  "V2RAY BY ZETA" ESPERE POR FAVOR......\e[1;m"
./instv2rayzeta/instalador.sh&> /dev/null && echo -e "\e[1;44mPANEL INSTALADO CON EXITO......\e[1;m"
sudo rm -rf instv2rayzeta  
while true; do
    read -p "¿DESEAS INSTALAR BADVPN (Necesario para juegos/videollamadas)? ESCRIBA YES o NO..."   yn
    case $yn in
        [Yy]* ) wget https://raw.githubusercontent.com/rockz5555/badvpn-installer/master/badvpn-installer.sh && bash badvpn-installer.sh; break;;
        [Nn]* ) echo -e "\e[1;41mELIGIO NO INSTALAR BADVPN, SI DESEA INSTALAR, REINSTALE SCRIPT......\e[1;m" && echo -e "\e[1;44mINSTALACION COMPLETADA......\e[1;m";exit;;
        * ) echo -e "\e[1;41mPOR FAVOR INGRESAR "YES" O "NO"......\e[1;m";;
    esac
done
  else echo -e "\e[1;41mINGRESE CON USUARIO ROOT......\e[1;m"                                                               
exit                                                                                 
fi
if [ "$EUID" = 0 ]                                                                   
  then echo -e "\e[1;44mINSTALACION COMPLETADA......\e[1;m"
sleep 2
echo -e "\e[1;44mINGRESE "V2RAY" PARA UTILIZAR EL PANEL ADMINISTRADOR......\e[1;m"
  else
    exit
      fi
