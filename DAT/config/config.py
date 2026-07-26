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

    # TODO: these vals should be declaritive answering "what" not "how"
    "luminosity": f"op.REACTION.op('OUT_luminosity')['energy'].eval()"

}