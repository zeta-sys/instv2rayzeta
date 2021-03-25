#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from v2ray_util import run_type

from ..util_core.v2ray import restart
from ..util_core.utils import readchar, random_email, ColorStr
from ..util_core.group import Vmess, Socks, Mtproto, SS
from ..util_core.writer import ClientWriter, GroupWriter
from ..util_core.selector import ClientSelector, GroupSelector

@restart()
def alterid():
    cs = ClientSelector(_('modify alterId'))
    group = cs.group

    if group == None:
        pass
    else:
        client_index = cs.client_index
        if type(group.node_list[client_index]) == Vmess:
            print("{}: {}".format(_("node alterID"), group.node_list[client_index].alter_id))
            new_alterid = input(_("INGRESE NUEVO alterID: "))
            if (new_alterid.isnumeric()):
                cw = ClientWriter(group.tag, group.index, client_index)
                cw.write_aid(int(new_alterid))
                print(_("alterID CAMBIADO CON EXITO!"))
                return True
            else:
                print(_("ERROR, REVISE LO INGRESADO"))
        else:
            print(_("SOLO EN PROTOCOLO VMESS PUEDE CAMBIAR alterID "))

@restart()
def dyn_port():
    gs = GroupSelector(_('modify dyn_port'))
    group = gs.group

    if group == None:
        pass
    else:
        print('{}: {}'.format(_("ESTADO DE PUERTO_DYN"), group.dyp))
        gw = GroupWriter(group.tag, group.index)
        choice = readchar(_("CAMBIAR A ABIERTO/CERRADO EL PUERTO_DYN(y/n): ")).lower()

        if choice == 'y':
            newAlterId = input(_("ELIJA PUERTO_DYN alterID(default 32): "))
            newAlterId = '32' if newAlterId == '' else newAlterId
            if (newAlterId.isdecimal()):
                gw.write_dyp(True, newAlterId)
                print(_("PUERTO DYN ABIERTO CON EXITO!"))
                return True
            else:
                print(_("ERROR, REVISE LO INGRESADO"))
        elif choice == 'n':
            gw.write_dyp(False)
            print(_("PUERTO DYN CERRADO CON EXITO!"))
            return True
        else:
            print(_("ERROR, INGRESE DE NUEVO"))

@restart()
def new_email():
    cs = ClientSelector(_('modify email'))
    group = cs.group

    if group == None:
        pass
    elif type(group.node_list[0]) == Socks:
        print(_("Socks5 NO SOPORTA REGISTRO DE EMAIL!!!"))
    else:
        client_index = cs.client_index
        group_list = cs.group_list
        print("{}: {}".format(_("node email"), group.node_list[client_index].user_info))
        email = ""
        while True:
            is_duplicate_email=False
            remail = random_email()
            tip = _("GENERANDO EMAIL ALEATORIO:") + ColorStr.cyan(remail) + _(", PRESIONE ENTER PARA USAR O INGRESE UNO NUEVO: ")
            email = input(tip)
            if email == "":
                email = remail
            from ..util_core.utils import is_email
            if not is_email(email):
                print(_("ERROR, NO ES UN EMAIL"))
                continue
            
            for loop_group in group_list:
                for node in loop_group.node_list:
                    if node.user_info == None or node.user_info == '':
                        continue
                    elif node.user_info == email:
                        print(_("ESTE EMAIL YA EXISTE, INGRESE OTRO"))
                        is_duplicate_email = True
                        break              
            if not is_duplicate_email:
                break

        if email != "":
            cw = ClientWriter(group.tag, group.index, client_index)
            cw.write_email(email)
            print(_("EMAIL CAMBIADO CON EXITO!!"))
            return True

@restart()
def new_uuid():
    cs = ClientSelector(_('modify uuid'))
    group = cs.group

    if group == None:
        pass
    else:
        client_index = cs.client_index
        if type(group.node_list[client_index]) == Vmess:
            print("{}: {}".format(_("node UUID"), group.node_list[client_index].password))
            choice = readchar(_("GENERAR NUEVO UUID?(y/n): ")).lower()
            if choice == "y":
                import uuid
                new_uuid = uuid.uuid1()
                print("{}: {}".format(_("NUEVO UUID"),new_uuid))
                cw = ClientWriter(group.tag, group.index, client_index)
                cw.write_uuid(new_uuid)
                print(_("UUID CAMBIADO CON EXITO!"))
                return True
            else:
                print(_("NO MODIFICADO"))
        else:
            print(_("SOLO EN PROTOCOLO VMESS SE PUEDE CAMBIAR EL UUID!"))

@restart(True)
def port():
    gs = GroupSelector(_('modify port'))
    group = gs.group

    if group == None:
        pass
    else:
        if group.end_port:
            port_info = "{0}-{1}".format(group.port, group.end_port)
        else:
            port_info = group.port
        print('{}: {}'.format(_("PUERTOS"), port_info))
        new_port_info = input(_("INGRESE NUEVO PUERTO - (PARA USAR UN RANGO DE PUERTOS USE '-' PARA SEPARAR, PARA QUE TENGA EFECTO):"))
        import re
        if new_port_info.isdecimal() or re.match(r'^\d+\-\d+$', new_port_info):
            gw = GroupWriter(group.tag, group.index)
            gw.write_port(new_port_info)
            print(_('PUERTO MODIFICADO CON EXITO'))
            return True
        else:
            print(_("ERROR!!!"))

@restart()
def tfo():
    gs = GroupSelector(_('modify tcpFastOpen'))
    group = gs.group

    if group == None:
        pass
    else:
        if type(group.node_list[0]) == Mtproto or type(group.node_list[0]) == SS:
            print(_("{} LOS PROTOCOLOS MTProto/Shadowsocks NO SOPORTAN TcpFastOpen!!!".format(run_type.capitalize())))
            print("")
            return
        
        print('{}: {}'.format(_("ESTADO tcpFastOpen"), group.tfo))
        print("")
        print(_("1.ABRIR TFO(FUERZA APERTURA)"))
        print(_("2.CERRAR TFO(FUERZA CIERRE)"))
        print(_("3.ELIMINAR TFO(use system default profile)"))
        choice = readchar(_("SELECCIONE POR FAVOR: "))
        if not choice:
            return
        if not choice in ("1", "2", "3"):
            print(_("ERROR, ELIJA UNA OPCION"))
            return
        
        gw = GroupWriter(group.tag, group.index)
        if choice == "1":
            gw.write_tfo('on')
        elif choice == "2":
            gw.write_tfo('off')
        elif choice == "3":
            gw.write_tfo('del')

        return True