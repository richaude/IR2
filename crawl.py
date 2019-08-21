from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, json, os
# vorher Bibliothek installieren: pip install elasticsearch
#from elasticsearch import Elasticsearch
#from elasticsearch.helpers import bulk

			
def findeAfD4(url, dictionaryList, rede_id):
	source = urlopen(url)
	bs = BeautifulSoup(source, "xml")
	for k in bs.findAll("kommentar"):
		k.decompose()
	for v in bs.findAll("vorname"):
		v.decompose()
	for n in bs.findAll("nachname"):
		n.decompose()
	for t in bs.findAll("titel"):
		t.decompose()
	for rede in bs.findAll("rede"):
		redeMeta = rede.find("p", {"klasse": "redner"})
		partei = redeMeta.find("fraktion")
		if partei != None and partei.text == "AfD":
			for p in rede.findAll("fraktion"):
				p.decompose()
			#print(rede.text)
			nameUsw = rede.find("p")
			if nameUsw.text[-7:] == " (AfD):":
				name = nameUsw.text[:-7]
				#datumUsw = bs.find("datum")
				#datum = datum.get("date")
				alleMetas = bs.find("dbtplenarprotokoll")
				sitzungsnummer = alleMetas.get("sitzung-nr")
				datum = alleMetas.get("sitzung-datum")
				eintragung = {"dokument_id": rede_id, "name":name, "datum":datum, "sitzungsnummer":sitzungsnummer, "rede":rede.text.strip()}
				dictionaryList.append(eintragung)
				rede_id += 1
			else:
				pass
	return rede_id
	
def mkJson3(filename):
	dictionaryList = []
	rede_id = 1
	for s in alleSitzungen():
		rede_id = findeAfD4(s, dictionaryList, rede_id)
	text = ""
	print(str(len(dictionaryList)))
	with open(filename, 'w', encoding='utf-8') as json_file:
		text += "{\n\"statements\":"
		text += json.dumps(dictionaryList, ensure_ascii=False)
		text+= "\n}"
		json_file.write(text)
		json_file.flush
		json_file.close
	print(str(rede_id))
			
def documents(filename, indexname):
    with open(filename, 'r') as file_handle:
        parsed_json = json.loads(file_handle.read())
        for document in parsed_json["statements"]:
            yield {
                "_index": indexname,
                "rede_id":document["dokument_id"],
                "name":document["name"],
                "datum":document["datum"],
                "sitzungsnummer":document["sitzungsnummer"],
                "rede":document["rede"],
                "_type": "_doc",
            }            
				
def alleSitzungen():
	return ["https://www.bundestag.de/resource/blob/543388/e95b7194470ed3c4e8bca546dd0da950/19001-data.xml"
			,"https://www.bundestag.de/resource/blob/543396/56cc6b4dac24ba9030170c178c68c953/19002-data.xml"
			,"https://www.bundestag.de/resource/blob/543394/3aaea6aea5bf07ea44c11b3020ba0ea3/19003-data.xml"
			,"https://www.bundestag.de/resource/blob/543402/a4ef1f16f734fb09d740843514d892ac/19004-data.xml"
			,"https://www.bundestag.de/resource/blob/543392/f3184e23eeb96ced9ea1abf61decf8bf/19005-data.xml"
			,"https://www.bundestag.de/resource/blob/543400/c1fc3b475c392769439b8440e81a8e15/19006-data.xml"
			,"https://www.bundestag.de/resource/blob/543398/6ed50213a4bd9891c9d48169a1bfcf17/19007-data.xml"
			,"https://www.bundestag.de/resource/blob/543390/856826b38825859f7871b1b2f1729eca/19008-data.xml"
			,"https://www.bundestag.de/resource/blob/543408/f9385a2e86d336a0c45a31ae51b3a5de/19009-data.xml"
			,"https://www.bundestag.de/resource/blob/543386/65dcdff3c104630a5e3b856c298063c2/19010-data.xml"
			,"https://www.bundestag.de/resource/blob/543406/b1e07adb71c9171e47d1f8ce5e74c7c8/19011-data.xml"
			,"https://www.bundestag.de/resource/blob/543404/d6be3032d02a2a5f0bcc49414923f27a/19012-data.xml"
			,"https://www.bundestag.de/resource/blob/544406/f9c38df1716131cde44014371481f2bc/19013-data.xml"
			,"https://www.bundestag.de/resource/blob/544630/58474a2534987e1c4b5b6c50e5d833ed/19014-data.xml"
			,"https://www.bundestag.de/resource/blob/544940/a1744cb7ee64ba09db6c3afabb8919f5/19015-data.xml"
			,"https://www.bundestag.de/resource/blob/545806/f217a39dc26097de7c9f860c992f610c/19016-data.xml"
			,"https://www.bundestag.de/resource/blob/546108/b7fad63a62d5e18631fa162d7587ff8d/19017-data.xml"
			,"https://www.bundestag.de/resource/blob/546402/7c1b0e613d69f3a8bd30ee461cf5ba19/19018-data.xml"
			,"https://www.bundestag.de/resource/blob/547472/ce5d79a3de7731d32430c008b8fbd2b1/19019-data.xml"
			,"https://www.bundestag.de/resource/blob/547714/716488e4055f7ceea64f1dadeec7eeb7/19020-data.xml"
			,"https://www.bundestag.de/resource/blob/548194/ae40c719c4658625f6a5734947321e26/19021-data.xml"
			,"https://www.bundestag.de/resource/blob/548526/feedd8065188d188fbd062575d7a0961/19022-data.xml"
			,"https://www.bundestag.de/resource/blob/548610/168e20b25cf8a98d4f5a1ee4c7a79090/19023-data.xml"
			,"https://www.bundestag.de/resource/blob/548910/1c3ab3b3333a175edc7b49f99b7ec19c/19024-data.xml"
			,"https://www.bundestag.de/resource/blob/550984/5d3779c013f2883f9bc199910b56cfe8/19025-data.xml"
			,"https://www.bundestag.de/resource/blob/551582/d4dda720393a825edd0b23b80239f0fa/19026-data.xml"
			,"https://www.bundestag.de/resource/blob/551584/96a3ba763db9633b76226c536f79d0aa/19027-data.xml"
			,"https://www.bundestag.de/resource/blob/553430/09007c2c517cdaa48eed1a6a6e988e95/19028-data.xml"
			,"https://www.bundestag.de/resource/blob/553878/7bc843a98b9782c2babf74e853c26198/19029-data.xml"
			,"https://www.bundestag.de/resource/blob/553876/400e0eb4b39f4d3e6146e1e8de99ce6f/19030-data.xml"
			,"https://www.bundestag.de/resource/blob/555136/2a0a890bbfadf8ebd6b44d091fa4aed0/19031-data.xml"
			,"https://www.bundestag.de/resource/blob/555518/f213ab11b90c2e4d5102315686f99971/19032-data.xml"
			,"https://www.bundestag.de/resource/blob/556388/6042eea504d93743f5160d3d18359f01/19033-data.xml"
			,"https://www.bundestag.de/resource/blob/556386/36c353e5fc4b7ad2c50ea72af3b146da/19034-data.xml"
			,"https://www.bundestag.de/resource/blob/558750/46669b434eef6ce7f6b2a396bb990539/19035-data.xml"
			,"https://www.bundestag.de/resource/blob/559034/ff15bafd34f97c81d1c4dd526d20ac97/19036-data.xml"
			,"https://www.bundestag.de/resource/blob/559390/51b31d124367ea20db898ce654964569/19037-data.xml"
			,"https://www.bundestag.de/resource/blob/560126/903fbf83a88cbf087678ab55aaf10a83/19038-data.xml"
			,"https://www.bundestag.de/resource/blob/560290/07510ac59444200dd9a0674a9e9c2791/19039-data.xml"
			,"https://www.bundestag.de/resource/blob/560634/63fa6bb716d47137393af638af3249bb/19040-data.xml"
			,"https://www.bundestag.de/resource/blob/562324/3ed065a2084ae77a4e45cd192f37ed29/19041-data.xml"
			,"https://www.bundestag.de/resource/blob/562712/fec082c4eb4bcd90d11773852b87524c/19042-data.xml"
			,"https://www.bundestag.de/resource/blob/562714/5e4e211a75972bcc22b8f37b455931fe/19043-data.xml"
			,"https://www.bundestag.de/resource/blob/562990/056c28051cb695642cb9d72521bba93b/19044-data.xml"
			,"https://www.bundestag.de/resource/blob/563214/4a6c01677b3e84af3b14da58b9045b25/19045-data.xml"
			,"https://www.bundestag.de/resource/blob/563398/99a2c9d4df10fcf44e67d084bf6c8f21/19046-data.xml"
			,"https://www.bundestag.de/resource/blob/568630/de702066295bfdf6ff6d3428442b7372/19047-data.xml"
			,"https://www.bundestag.de/resource/blob/568698/e7948fb5290d145a30b829b80051d9e5/19048-data.xml"
			,"https://www.bundestag.de/resource/blob/568832/d8d8814b76922dfca2171c55c2c04d28/19049-data.xml"
			,"https://www.bundestag.de/resource/blob/569484/48b47af3bcd1fd45af0c0c6a3c8d62be/19050-data.xml"
			,"https://www.bundestag.de/resource/blob/570646/4659347802289f5b38758ecfb386e6ba/19051-data.xml"
			,"https://www.bundestag.de/resource/blob/570844/a618e08538ff1f10265ff35f82131381/19052-data.xml"
			,"https://www.bundestag.de/resource/blob/571420/17bc3eab3abd22795c9d55876a2f4dde/19053-data.xml"
			,"https://www.bundestag.de/resource/blob/572934/1e36d1dfea802b345a63b8dc19f21485/19054-data.xml"
			,"https://www.bundestag.de/resource/blob/573482/27dfa5aa469fc1c5ed915e6a0900d878/19055-data.xml"
			,"https://www.bundestag.de/resource/blob/573822/41ceeb62a53b1b7c6a247aabf38f8136/19056-data.xml"
			,"https://www.bundestag.de/resource/blob/574574/fc1602280bc4c1fbfa6269f92a5a5342/19057-data.xml"
			,"https://www.bundestag.de/resource/blob/574826/0e3659e11c1c3cdbfa621369cd16735a/19058-data.xml"
			,"https://www.bundestag.de/resource/blob/575138/b5395a975d1c55838da0e52251018160/19059-data.xml"
			,"https://www.bundestag.de/resource/blob/577622/da97888b713abb16ed2070836504b83a/19060-data.xml"
			,"https://www.bundestag.de/resource/blob/577958/e2063c0f51a32690a269f48aa6102c1d/19061-data.xml"
			,"https://www.bundestag.de/resource/blob/578466/7430bccaf792e7bc55e84d5e64675820/19062-data.xml"
			,"https://www.bundestag.de/resource/blob/579752/52470466623d8cd77b3a895e807eff51/19063-data.xml"
			,"https://www.bundestag.de/resource/blob/579978/cd4658159cdb20e26173e6e966e915c9/19064-data.xml"
			,"https://www.bundestag.de/resource/blob/580166/a0b286a19709f1d05a25641745e7a2e4/19065-data.xml"
			,"https://www.bundestag.de/resource/blob/580518/00257b7bcc8f4be391134476276cf037/19066-data.xml"
			,"https://www.bundestag.de/resource/blob/581206/e5a0245d75a35edd81d70d383bcb27cd/19067-data.xml"
			,"https://www.bundestag.de/resource/blob/581444/3930891e2db9b2f3b95b195bba2c11c9/19068-data.xml"
			,"https://www.bundestag.de/resource/blob/581712/62c198b012ccf56048572e505fdf2a26/19069-data.xml"
			,"https://www.bundestag.de/resource/blob/584216/abd88b9482e7b1372c58aa5b5bec91f2/19070-data.xml"
			,"https://www.bundestag.de/resource/blob/584494/326fdeb98c9a489cda59dd80d5a41c51/19071-data.xml"
			,"https://www.bundestag.de/resource/blob/584722/63ec7645124cdb4dadeeb961b4c3dee0/19072-data.xml"
			,"https://www.bundestag.de/resource/blob/588382/827178442054afb8591464af3d465a18/19073-data.xml"
			,"https://www.bundestag.de/resource/blob/588878/369ec79a1c163848fdf5fccfe5b912d7/19074-data.xml"
			,"https://www.bundestag.de/resource/blob/588928/87b7d62ef70f4397a73ff42d504bd3fe/19075-data.xml"
			,"https://www.bundestag.de/resource/blob/590370/9e0d3cbabe0de056e83d2b0dad01e575/19076-data.xml"
			,"https://www.bundestag.de/resource/blob/590790/05a7414dbbd0e7d3d339679d09b79229/19077-data.xml"
			,"https://www.bundestag.de/resource/blob/591118/15afa3cf3897559856c30498403f473f/19078-data.xml"
			,"https://www.bundestag.de/resource/blob/593318/95d4caa1b22309ab33d462f56f21c9c3/19079-data.xml"
			,"https://www.bundestag.de/resource/blob/593816/6a0ddcfe1966e250ebdbac4759bfeb68/19080-data.xml"
			,"https://www.bundestag.de/resource/blob/594190/bcb075a7b42209146a684802b7c64bb2/19081-data.xml"
			,"https://www.bundestag.de/resource/blob/595050/82a69f72a6621dd4571680704361cff9/19082-data.xml"
			,"https://www.bundestag.de/resource/blob/595300/707c0bea31cc2b599cc68cba83542996/19083-data.xml"
			,"https://www.bundestag.de/resource/blob/597788/dedf063d6567225a318dab8799a6571d/19084-data.xml"
			,"https://www.bundestag.de/resource/blob/628694/3a780577a4e55da0bd3d436e5190ec4c/19085-data.xml"
			,"https://www.bundestag.de/resource/blob/629172/b6278747e2ac4bbcd81a580744dd3efc/19086-data.xml"
			,"https://www.bundestag.de/resource/blob/629642/f0f28ffcf1a7a6aff183bdc5fcb89040/19087-data.xml"
			,"https://www.bundestag.de/resource/blob/630646/2d50ffba980dcde74edbc43ece73f16d/19088-data.xml"
			,"https://www.bundestag.de/resource/blob/630970/e1a88c9b91e7a2163d869c8643f578cb/19089-data.xml"
			,"https://www.bundestag.de/resource/blob/631398/0ecf52bec9e3013b279ae31b912b2815/19090-data.xml"
			,"https://www.bundestag.de/resource/blob/633554/21103de8050b0dbe32bede09351427de/19091-data.xml"
			,"https://www.bundestag.de/resource/blob/633894/82eaee2230a1e625bfee3d4a25143ea9/19092-data.xml"
			,"https://www.bundestag.de/resource/blob/634260/b7b9a9a031fc0dcbe5fae559d2b9581a/19093-data.xml"
			,"https://www.bundestag.de/resource/blob/635190/f6c4b7ff7cb9dab7d3499116be7d67c9/19094-data.xml"
			,"https://www.bundestag.de/resource/blob/635514/4915f30b7a6284b1f9159f0b95104d65/19095-data.xml"
			,"https://www.bundestag.de/resource/blob/635932/c2426bdb65d7398765ab8456fe0c47c8/19096-data.xml"
			,"https://www.bundestag.de/resource/blob/641364/22d579d683d89b1bcf27bd8ca7dd6be6/19097-data.xml"
			,"https://www.bundestag.de/resource/blob/641838/a20491b431845ac9b4c90aeaeb29ffda/19098-data.xml"
			,"https://www.bundestag.de/resource/blob/642190/c1267dc263835ae5407b1838148921dd/19099-data.xml"
			,"https://www.bundestag.de/resource/blob/643514/426ecc04b50e2907ff07cb0e18606f76/19100-data.xml"
			,"https://www.bundestag.de/resource/blob/643544/58512be83d12c1788a26350196d0c538/19101-data.xml"
			,"https://www.bundestag.de/resource/blob/643856/580ac0e72309db52b8912be3d15f028b/19102-data.xml"
			,"https://www.bundestag.de/resource/blob/646184/797a77b5df970d80599787912838cf4b/19103-data.xml"
			,"https://www.bundestag.de/resource/blob/646486/a7a98a31f88a05844761049e113f0601/19104-data.xml"
			,"https://www.bundestag.de/resource/blob/646890/4385b458c9de31d2cf3c0c3f01895d57/19105-data.xml"
			,"https://www.bundestag.de/resource/blob/649756/618b8c8527fab3ec3c07843a90006aa1/19106-data.xml"
			,"https://www.bundestag.de/resource/blob/649826/5d46e129568d1b918d818b5d595ce0ab/19107-data.xml"
			,"https://www.bundestag.de/resource/blob/650092/451aa625206cceec8b3c2d4955b49f25/19108-data.xml"
			,"https://www.bundestag.de/resource/blob/652630/45d3afd3d973978b75581d3ed89c8afd/19109-data.xml"
			]

	
mkJson3("protokolle5.json")
#es = Elasticsearch()
#bulk(es, documents("protokolle5.json", "new_index3"))
