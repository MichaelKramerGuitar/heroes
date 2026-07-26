PROJECT = {

    "name": "Heroes"

}


AUDIO = {

    "device": "Focusrite",

    "driver": "ASIO"

}

PORTRAITS = {

    "monk": "assets/monk.jpg",

    "coltrane": "assets/coltrane.jpg",

    "mingus": "assets/mingus.jpg"

}

PORTRAIT = {

    "hero": PORTRAITS.get("monk")

}


REACTION = {

    "luminosity": f"op.REACTION.op('OUT_luminosity')['energy'].eval()"

}