# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "bienvenidos a las eskills mamalonas de coches, musica y educacion "
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class versiones(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("versiones")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = "tiene varias versiones, civic, city, accord, crv, rav4."
            
        if consola_name == "toyota":
            consola_datos = " tiene varias versiones, cambry,corrolla,hillux,sieenna."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class malasletras(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("malasletras")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "aleman":
            consola_datos = "Lalala, lalala Lala, jaja Uh, A-L-E-M-Á-N Ya valió , Alemán ahí viene Todos corran rápido, un virus en mi ADN Provoca que todos me quieran  Tutto bene, puto el nene Lloriqueando por envidia de lo que no tiene Por copión no hagas que te condene Tiran mucho aceite, pero aceite Mennen Uh, A-L-E-M-Á-N"
            
        if consola_name == "geramx":
            consola_datos = "Salí corriendo de los torres, era el más pequeño Con tantas inquietudes la calle me quitó el sueño Mis letras son diamantes van a la casa de empeño Y no soy bienvenido en casa desde que prendí ese leño Rosario está dormida y no Tuve tiempo para despedirme, lo lamento, hoy Quiero volver nena, fui a buscar comida Y sé que tú ni yo, pedimos esta perra vida"
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class albums(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("albums")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "geramx":
            consola_datos = "tiene varios albums, los niños grandres no juegan, vicio y fama, ahora tengo todo."
            
        if consola_name == "aleman":
            consola_datos = " tiene varios albums, huracan,eclipse,rolemos otro"
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class letras(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("letras")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "geramx":
            consola_datos = "Estaba pensando en llamarte, yo te miro por todas partes Pero ya no nos vemos, puede que lo olvidemos Dos tragos y vuelvo a pensarte Me aferro, no quiero olvidarte Sentimientos ajenos, los celos no son buenos Y si me llamas contesto, aunque nunca va a pasar eso (Aunque nunca va a pasar eso) Ya mejor ni te molesto, porque sé que vuelvo a joderlo (Ahuevo que vuelvo a joderlo)."
            
        if consola_name == "aleman":
            consola_datos = " Me preguntan Alemán como le haces pa' rimar La verdad que no lo se pero mira carnal Vengo de un planeta muy lejano mas allá Que tu pinche imaginación pueda crear A mi no me quiera verbear Mucho menos puede con ninguno de mi gang Todo mi clika parece del west Original gangsta a los 16 Pues qué pues No no me quiere ganar Pues qué pues"
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"

class informacion(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("informacion")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "geramx":
            consola_datos = "Pertenecia a la mexamafia pero se  hizo independiente."
            
        if consola_name == "aleman":
            consola_datos = " Es un cantante llamado erick conocido como aleman nacido en cabo san locos."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"

class musica(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("musica")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "geramx":
            consola_datos = "las mas escuchadas son Botella tras botella y Plasticos."
            
        if consola_name == "aleman":
            consola_datos = " las mas escuchadas son pues que pues y categoria 5."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class carros(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("carros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = " tiene un auto iconico NSX."
            
        if consola_name == "toyota":
            consola_datos = " tiene un auto iconico Supra."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class vendido(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("vendido")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = " El auto mas vendido es la CRV."
            
        if consola_name == "toyota":
            consola_datos = "El auto mas vendido es el corrolla."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class menosvendido(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("menosvendido")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = " El auto menos vendido es el jazz."
            
        if consola_name == "toyota":
            consola_datos = "El auto menos vendido es el pryus."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class supra(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("supra")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un motor 2JZ twin turbo."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 7 velocidades o una automatica doble embrague."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class brz(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("brz")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un Motor de inyección directa e indirecta y 2.4 litros SUBARU BOXER.."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una  transmisión manual de 6 marchas o a una automática con el mismo número de relaciones. ."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class skyline(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("skyline")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor I6 doble turbo RB26DETT."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades 6-speed Getrag 233 manual."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class nsx(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("nsx")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un motor V6 de 3,2 litros aunque subía la potencia a los 290 CV."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision 	Semiautomática de doble embrague de 9 velocidades."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class mustang(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("mustang")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor  V8 4.6 y 305 CV de potencia máxima.."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision de 5 marchas, transmisión manual."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class camaro(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("camaro")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor MOTOR LT1 V8 DE 6.2 L.."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades automatica y manual."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class vocho(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("vocho")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 1600i de 46 Hp con convertidor catalítico."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 5 velocidades y reversa."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class ranger(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ranger")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 4 cilindros de 2.5 ltrs."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 5 velocidades y reversa."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class lobo(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lobo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor v8 triton de 5.4 ltrs."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision automatica de 5 velocidades doble drive y reversa."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class corrolla(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("corrolla")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 4 cilindros 2.0 ltrs."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades y una automatica doble enbrague."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class camry(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("camry")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 2.5 L 4 motor en línea."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision auto de 6 velocidades transmission gearbox.."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class civic(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("civic")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor gasolina de 1799 cc con 4 cilindros ubicados en línea que alcanza una potencia máxima de 140 CV a 6300 rpm."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades de cvt."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class accord(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("accord")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motorgasolina de 1799 cc con 4 cilindros ubicados en línea que alcanza una potencia máxima de 140 CV a 6300 rpm turbo."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision automatica de 6 velocidades ."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class crv(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("crv")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 1.5 turbo de 193 CV y 243 Nm."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar y automatica de 6 velocidades cvt."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class hilux(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("hilux")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor  motor 2.7 l 4 motor en línea."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades ."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class frontier(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("frontier")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un motor 2.5 l 4 motor en línea."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades y automatica."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class avalon(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("avalon")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 3.5 V6 (268 CV) ECT-i."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades "
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class lancer(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lancer")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor 2.4 litros de 170 CV."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades y automatica."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class eclipse(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("eclipse")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un motor 4G63.."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class aventador(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aventador")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor central de 12 cilindros, de 6 litros y medio de cilindrada y 740 CV de potencia a 8.400 rpm."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision automatica que Tiene siete velocidades, es de un solo embrague pero cambia en 50 milisegundos."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class bugatti(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("bugatti")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor un W16 de 8.0 litros con cuatro turbocompresores."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision De doble embrague DSG de 7 velocidades."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class avenger(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("avenger")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor  V6 PENTASTAR® DE 3.6 LITROS y 283 CABALLOS PARA UN MANEjO."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision estandar de 6 velocidades 6-speed Getrag 233 manual."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class charger(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("charger")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor MOTOR HEMI® V8 de 5.7L.."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision automática de 8 velocidades."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class challenger(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("challenger")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["detalles"].value
        if consola_name == "motor":
            consola_datos = " El auto tiene un  motor HEMI® V8 6.2L supercargado de alta potencia despliega 807 caballos de fuerza."
            
        if consola_name == "trasmision":
            consola_datos = "El auto tiene una trasmision automática de 8 velocidades."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class kiddkeo(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("kiddkeo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 52 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class aleman(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aleman")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 58 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class geramx(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("geramx")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 66 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class eladiocarrion(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("eladiocarrion")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 85 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Urbano latino."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class bizzarap(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("bizzarap")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = "50 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Urbano latino."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class zxmyr(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("zxmyr")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 25 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class badbunny(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("badbunny")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 97 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "regueton."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class dadyyanke(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("dadyyanke")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 67 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "regueton."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class planB(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("planB")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 112 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "regueton."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class carteldesanta(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("carteldesanta")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 152 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class sandromalandro(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("sandromalandro")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 35 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class santafe(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("santafe")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 75 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop/rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class relsb(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("relsb")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = "62 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Urbano latino."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class munichb(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("munichb")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 15 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Hip-hop."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class donomar(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("donomar")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 369 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "Urbano latino y regueton."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class aldotrujillo(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aldotrujillo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 58 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "corridos."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class maxrc(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("maxrc")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 30 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "trap rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class toserone(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("toserone")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 34 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "trap rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class ibarra(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ibarra")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["artistas"].value
        if consola_name == "total de canciones":
            consola_datos = " 27 canciones en total."
            
        if consola_name == "genero musical ":
            consola_datos = "trap rap."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"

class caracteristicas(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("caracteristicas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " Los procesadores AMD Ryzen 3000 series ofrecen una excelente potencia para todo tipo de actividades. Su arquitectura Zen 2 de alto rendimiento ofrece velocidades turbo máximas de 4,0 GHz y acceso más rápido a la memoria, lo que mejora el rendimiento en la ejecución de múltiples tareas."
            
        if consola_name == "tarjetagrafica":
            consola_datos = " la APU más potente fabricada por el Team Red con arquitectura Zen 3 y 7 nm. Cuenta con 8 núcleos físicos y 16 lógicos, esta vez integrados en un solo chip junto a los gráficos Radeon Vega de 8 núcleos a 2000 MHz.."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class ventamayor(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ventamayor")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " Ryzen 7 2700X "
        if consola_name == "tarjetagrafica":
            consola_datos = "	Radeon RX 5700 XT"
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class ventamenor(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ventamenor")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " Ryzen 3 1300X "
        if consola_name == "tarjetagrafica":
            consola_datos = "	radeon vega 3"
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class prigeneracion(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("prigeneracion")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " Ryzen 3 1200, Ryzen 5 1600, Ryzen 7 1700 "
        if consola_name == "tarjetagrafica":
            consola_datos = "	Ryzen 5 3400G y Ryzen 3 3200G, que son los sucesores de los 2400G y 2200G de la generación anterior"
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class ultimageneracion(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ultimageneracion")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " Todos los procesadores AMD Ryzen™ de la serie 5000 incluyen las tecnologías de procesamiento innovadoras que caracterizan la familia Ryzen™. "
        if consola_name == "tarjetagrafica":
            consola_datos = "Gráficos Radeon 7, S-AM4, 3.90GHz, Six-Core, 16MB L3 Caché"
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class totalvendidos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("totalvendidos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ryzen"].value
        if consola_name == "procesador":
            consola_datos = " 97 millones de unidades vendidas "
        if consola_name == "tarjetagrafica":
            consola_datos = "más de 50 millones de tarjetas gráficas"
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
"--------------------------------------------------------"
class color(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("color")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = " tiene 3 colores principales el rojo, negro y azul."
            
        if consola_name == "toyota":
            consola_datos = "  tiene 3 colores principales el blanco, negro y gris."
            
               
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    "-------------------------------------------------------------------------------------"
    
class tipos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("tipos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcas"].value
        if consola_name == "honda":
            consola_datos = " tiene varios tipos, como camionestas, deportivos, hatchback,sedan,motos."
            
        if consola_name == "toyota":
            consola_datos = " tiene varios tipos, como sedanes, camionestas, deportivos, hatchback."
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    "-------------------------------------------------------------------------------------"
    
class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(carros())
sb.add_request_handler(color())
sb.add_request_handler(tipos())
sb.add_request_handler(informacion())
sb.add_request_handler(musica())
sb.add_request_handler(versiones())
sb.add_request_handler(albums())
sb.add_request_handler(letras())
sb.add_request_handler(malasletras())
sb.add_request_handler(menosvendido())
sb.add_request_handler(vendido())
sb.add_request_handler(ventamenor())
sb.add_request_handler(ventamayor())
sb.add_request_handler(caracteristicas())
sb.add_request_handler(prigeneracion())
sb.add_request_handler(ultimageneracion())
sb.add_request_handler(totalvendidos())
sb.add_request_handler(supra())
sb.add_request_handler(skyline())
sb.add_request_handler(nsx())
sb.add_request_handler(mustang())
sb.add_request_handler(camaro())
sb.add_request_handler(vocho())
sb.add_request_handler(ranger())
sb.add_request_handler(lobo())
sb.add_request_handler(corrolla())
sb.add_request_handler(camry())
sb.add_request_handler(civic())
sb.add_request_handler(accord())
sb.add_request_handler(crv())
sb.add_request_handler(hilux())
sb.add_request_handler(frontier())
sb.add_request_handler(avalon())
sb.add_request_handler(lancer())
sb.add_request_handler(eclipse())
sb.add_request_handler(aventador())
sb.add_request_handler(bugatti())
sb.add_request_handler(avenger())
sb.add_request_handler(charger())
sb.add_request_handler(challenger())
sb.add_request_handler(brz())
sb.add_request_handler(kiddkeo())
sb.add_request_handler(aleman())
sb.add_request_handler(geramx())
sb.add_request_handler(eladiocarrion())
sb.add_request_handler(bizzarap())
sb.add_request_handler(zxmyr())
sb.add_request_handler(badbunny())
sb.add_request_handler(dadyyanke())
sb.add_request_handler(planB())
sb.add_request_handler(carteldesanta())
sb.add_request_handler(sandromalandro())
sb.add_request_handler(santafe())
sb.add_request_handler(relsb())
sb.add_request_handler(munichb())
sb.add_request_handler(donomar())
sb.add_request_handler(aldotrujillo())
sb.add_request_handler(maxrc())
sb.add_request_handler(toserone())
sb.add_request_handler(ibarra())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()