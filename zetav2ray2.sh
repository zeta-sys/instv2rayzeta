#!/bin/bash
# Author: Zeta
git clone https://github.com/zeta-sys/instv2rayzeta.git
chmod 777 instv2rayzeta/instalador.sh
echo $to_print
	to_print='INSTALANDO  "V2RAY BY ZETA" ESPERE POR FAVOR......'
	echo $to_print
./instv2rayzeta/instalador.sh&> /dev/null && echo INSTALACION FINALIZADA || echo FALLO INSTALACION
sudo rm -rf instv2rayzeta  
while true; do
    read -p "¿DESEAS INSTALAR BADVPN (Necesario para juegos/videollamadas)? ESCRIBA YES o NO..."   yn
    case $yn in
        [Yy]* ) wget https://raw.githubusercontent.com/rockz5555/badvpn-installer/master/badvpn-installer.sh && bash badvpn-installer.sh; break;;
        [Nn]* ) echo "DIGITE "V2RAY" PARA INCIAR - QUE LO DISFRUTE  :)";exit;;
        * ) echo "Por favor responde \"yes\" para si o \"no\"";;
    esac
done

to_print='INSTALACION FINALIZADA CON EXITO....   ;-)'
	echo $to_print
	to_print='DIGITE  "V2RAY"  PARA ENTRAR AL PANEL ADMINISTRADOR......'
	echo $to_print
