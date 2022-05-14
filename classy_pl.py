""" classy classification, eksperyment z klasyfikacją krótkich tekstów """
import spacy
import classy_classification

data = {
    "długi": ["tenże Spytek dopisuje temuż 62 grz. długu do sumy 100 grz. na dobrach w B.",
              "Jan z Melsztyna ręczy za dług 1150 fl. Pawłowi Czarnemu z Witowic, m. in. wsią B.",
              "Werner z → Bilska poręcza za dług Jakuba z Dębna Janowi Wielopolskiemu bachmistrzowi w Bochni, m. in. wsią C.",
              "Piotr starszy s. pkom. krak. Piotra z Pieskowej Skały pożycza 500 fl. węg. od Szczepana z Pogórzyc tenut. będzińskiego, które Szczepan dolicza sobie do sumy zapisanej mu przez zm. Piotra Szafrańca na dobrach B. Będzie też miał doliczone do sumy zastawu nakłady na naprawę zamku i murów. Piotr potwierdza mu też 2 grz. z cła krak. dawane do zamku B., a które ojciec zapisał Szczepanowi. Piotr poręcza za młodszych br.: Krzysztofa, Stanisława i Piotra"
                 ],
    "sprzedaż":  ["Jan sprzedaje Mik. Jordanowi z Zakliczyna kaszt. wojnickiemu zamek Melsztyn z wsiami, m. in. B.",
                 "tenże sprzedaje za 22 grz. z rocznym pr. wykupu szl. Wojciechowi włodarzowi z Witkowic gaj w A. zw. Kozilas (Kozylasch) między Sulisławicami, Lgotą i Trzebienicami",
                 "Mik. Pieniążek z Iwanowic sprzedaje za 1000 zł Pawłowi Czarnemu z Witowic A., Szreniawę i Wierzchowiska"
                ]
}

# nlp = spacy.load('pl_core_news_lg')
# nlp.add_pipe(
#         "text_categorizer",
#         config={
#             "data": data,
#             "model": "spacy"
#         }
# )

nlp = spacy.blank("pl")
nlp.add_pipe(
    "text_categorizer",
    config={
        "data": data,
        #"model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "model": "inovex/multi2convai-logistics-pl-bert",
        "device": "cpu"
    }
)

print(nlp("Mikołaj z Budziszowic sprzedaje za 400 grz. i konia karczmę i las Janowi z Lęborka.")._.cats)
print(nlp("Stanisław Jelitko z Podstolic oznajmia, że Mikołaj z Białej kaszt. wojnicki ma dług 500 fl.")._.cats)
print(nlp("Jan z Chełmna odsprzedał Bożęcie z Budy młyn wraz ze stawem.")._.cats)
print(nlp("Mikołaj z Bielska kasztelan wojnicki spłaca dług 100 grz. Sławnikowi ze Śladowa")._.cats)
print(nlp("Mikołaj z Białej kasztelan wojnicki przyrzeka sprzedać wieś Jodłowa Sławnikowi ze Śladowa")._.cats)

# Wyniki:
# {'długi': 0.10711425660604079,  'sprzedaż': 0.8928857433939593}
# {'długi': 0.8376264035727088,   'sprzedaż': 0.16237359642729135}
# {'długi': 0.12288104481506047,  'sprzedaż': 0.8771189551849397}
# {'długi': 0.6674496823840843,   'sprzedaż': 0.33255031761591575}
# {'długi': 0.009693355618132183, 'sprzedaż': 0.9903066443818678}
