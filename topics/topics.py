import json

topics = [
{
  "id" : "001",
  "title" : "Brexit",
  "description" : "What's the opinion of the AfD towards Brexit?",
  "narrative" : "Relevant documents must include a judgement of all the happenings and processes about Brexit."
},
{
  "id" : "002",
  "title" : "no deal brexit",
  "description" : "How does the AfD anticipate a no deal Brexit?",
  "narrative" : "Relevant documents must include the special case of a Brexit without any treaties."
},
{  
  "id" : "003",
  "title" : "G20",
  "description" : "How are all international events like G20 judged by the AfD?",
  "narrative" : "Relevant documents must include mentions of international meetings, especially the G20."
},
{
  "id" : "004",
  "title" : "Merkel",
  "description" : "How does the AfD anticipate Merkels style of governing",
  "narrative" : "Relevant documents must adress Merkel or talk about aspects of her policies."
}, 
{
  "id" : "005",
  "title" : "Arbeitslose",
  "description" : "How does the AfD see the situation in the countries for people who have no jobs?",
  "narrative" : "relevant documents must speak about people who have no jobs and plans to better conditions for them"
},
{
  "id" : "006",
  "title" : "Sachsen",
  "description" : "How does the AfD think about the federal state of Saxonia",
  "narrative" : "Relevant documents must adress Sachsen in particular, it has to stand out in the speech, among the other states"
},
{
  "id" : "007",
  "title" : "Bildung",
  "description" : "How important is education for the AfD",
  "narrative" : "Relevant documents must include plans for public education or a description of current conditions"
},
{
  "id" : "008",
  "title" : "Digitalisierung",
  "description" : "How important is digitalisation for the AfD",
  "narrative" : "Relevant documents must include plans for further digitalisation or a description of current conditions."
},
{
  "id" : "009",
  "title" : "linksgrün",
  "description" : "in which kind of contexts does the AfD use \"linksgrün\"",
  "narrative" : "The assumption is that they will make overt use of this word, so relevant documents must feature this word in prominent places."
},
{
  "id" : "010",
  "title" : "Linksextreme",
  "description" : "To which extent do AfD members speak about extremism from the far left?",
  "narrative" : "relevant documents must include broad discussions about the danger of left wing extremism"
},
{
  "id" : "011",
  "title" : "Rechtsextreme",
  "description" : "To which extent do AfD members speak about extremism from the far right?",
  "narrative" : "relevant documents must include broad discussions about the danger of right wing extremism"
},
{
  "id" : "012",
  "title" : "Bundeswehr",
  "description" : "How does the AfD see the current Bundeswehr",
  "narrative" : "relevant documents include plans for the Bundeswehr or a description of the current conditions"
},
{
  "id" : "013",
  "title" : "Sexualität",
  "description" : "In which way does the AfD speak about sexuality?",
  "narrative" : "relevant documents mention different aspects of sexual orientation or preferences"
},
{
  "id" : "014",
  "title" : "gender",
  "description" : "How does the AfD see gender studies?",
  "narrative" : "relevant documents must include mentions of the \"gender\" buzzword."
},
{
  "id" : "015",
  "title" : "Landwirtschaft",
  "description" : "How does the AfD see farmers and agriculture",
  "narrative" : "relevant documents must include issues adressing agriculture"
},
{
  "id" : "016",
  "title" : "Seehofer",
  "description" : "What does the AfD think about politician Seehofer",
  "narrative" : "relevant documents must mention or adress Seehofer in a peculiar fashion that makes his name stand out"
},
{
  "id" : "017",
  "title" : "Seenotrettung",
  "description" : "How does the AfD see the issue of saving people in the oceans and how do they judge people who actively volunteer to save drowning people",
  "narrative" : "relevant documents must mention sea rescue as main topic of speech"
},
{
  "id" : "018",
  "title" : "Flüchtlinge",
  "description" : "How does the AfD see immigrants?",
  "narrative" : "relevant documents must speak about refugees as the main topic of discourse"
},
{
  "id" : "019",
  "title" : "kriminell",
  "description" : "In which context does this word occur in an AfD Speech?",
  "narrative" : "relevant documents contain this word or a semantically similar in repeated phrasing and context"
},
{
  "id" : "020",
  "title" : "Medien",
  "description" : "What's the AfD's opinion on the media?",
  "narrative" : "relevant documents mention the perception of all kinds of media by the AfD as the main topic"
},
{
  "id" : "021",
  "title" : "Waffen",
  "description" : "When do AfD members mention weapons",
  "narrative" : "relevant documents mention any kind of weapons, either smaller ones like guns and pistols, but also nuclear weapons"
},
{
  "id" : "022",
  "title" : "Schulen",
  "description" : "How do AfD members speak of schools",
  "narrative" : "relevant documents adress the current situation of public schools as a main issue"
},
{
  "id" : "023",
  "title" : "Putin",
  "description" : "Which speeches talk about the Russian President Vladimir Putin?",
  "narrative" : "relevant documents must be about Putin, not among other heads of state, but especially about him"
},
{
  "id" : "024",
  "title" : "Trump",
  "description" : "Which speeches talk about the American President Donald Trump?",
  "narrative" : "relevant documents must be about Putin, not among other heads of state, but especially about him and his leading style"
},
{
  "id" : "025",
  "title" : "USA",
  "description" : "When are the United States of America mentioned by members of the AfD?",
  "narrative" : "relevant documents include peculiar mentions of the USA"
},
{
  "id" : "026",
  "title" : "Russland",
  "description" : "Which speeches talk about Russia?",
  "narrative" : "relevant documents talk in a stand out fashion about Russia and/or the Russian Federation"
},
{
  "id" : "027",
  "title" : "Wahl",
  "description" : "Which elections are mentioned by the AfD, what kind of aspects are spoken about",
  "narrative" : "relevant documents speak about elections and the election process in particular"
},
{
  "id" : "028",
  "title" : "Demokratie",
  "description" : "How is democracy valued by the AfD",
  "narrative" : "relevant documents talk about character and importance of a well functioning democracy"
},
{
  "id" : "029",
  "title" : "Wahlbeeinflussung",
  "description" : "Does the AfD cover election meddling in their speeches",
  "narrative" : "relevant documents talk about the dangers of election meddling and undermining of democratic values in a stand out fashion"
},
{
  "id" : "030",
  "title" : "Gauland",
  "description" : "What kind of speeches are delivered by AfD politician Gauland, what kind of other speeches mention him?",
  "narrative" : "relevant documents are speeches by Gauland or speeches that mention him"
},
{
  "id" : "031",
  "title" : "Weidel",
  "description" : "What kind of speeches are delivered by AfD politician Weidel, what kind of other speeches mention her",
  "narrative" : "relevant documents are speeches by Weidel or speeches that mention her"
},
{
  "id" : "032",
  "title" : "Feminismus",
  "description" : "How does the AfD see feminism?",
  "narrative" : "relevant documents include feminism as a main topic, and a judgement made by the AfD, about it"
},
{
  "id" : "033",
  "title" : "Universitäten",
  "description" : "what does the AfD say about universities",
  "narrative" : "relevant documents include a description of problems or other issues, the AfD sees in universities in particular"
},
{
  "id" : "034",
  "title" : "DDR",
  "description" : "How and when does the AfD talk about the German Democratic Republic",
  "narrative" : "relevant documents mention the GDR in particular"
},
{
  "id" : "035",
  "title" : "1989",
  "description" : "How does the AfD see the events that took place in 1989?",
  "narrative" : "relevant documents mention the year 1989 and it's meaning for AfD members"
},
{
  "id" : "036",
  "title" : "Bannon",
  "description" : "Is US far right activist Steve Bannon mentioned in the Bundestag?",
  "narrative" : "relevant documents mention Steve Bannon"
},
{
  "id" : "037",
  "title" : "Osteuropa",
  "description" : "Is eastern Europe mentioned during an AfD speech",
  "narrative" : "relevant documents include mentions of eastern Europe in specific"
},
{
  "id" : "038",
  "title" : "Krieg",
  "description" : "How and with which kind of connotation is talked about war in an AfD speech",
  "narrative" : "relevant documents include mentions of any war or conflict as main issue"
},
{
  "id" : "039",
  "title" : "Rassismus",
  "description" : "When does the AfD mention racism",
  "narrative" : "relevant documents mention racism and talk about it in a stand out fashion"
},
{
  "id" : "040",
  "title" : "Antifaschismus",
  "description" : "When and how does the AfD speak about antifascism",
  "narrative" : "relevant documents mention and talk in a stand out fashion about antifascism"
},
{
  "id" : "041",
  "title" : "die NATO",
  "description" : "How is the NATO seen by the AfD",
  "narrative" : "relevant documents talk about the NATO in a stand out fashion"
},
{
  "id" : "042",
  "title" : "Nazis",
  "description" : "Does the AfD talk about Nazis",
  "narrative" : "relevant documents mention this term, which is rather colloquial for parliaments speech"
},
{
  "id" : "043",
  "title" : "Hitler",
  "description" : "Does the AfD ever mention Hitler",
  "narrative" : "relevant documents mention Hitler"
},
{
  "id" : "044",
  "title" : "drittes Reich",
  "description" : "Do AfD members speak about the Nazi regime, using this propaganda term?",
  "narrative" : "relevant documents explicitly mention this term"
},
{
  "id" : "045",
  "title" : "Klimawandel",
  "description" : "Does the AfD ever adress climate change",
  "narrative" : "relevant documents mention the issue of climate change in a stand out fashion"
},
{
  "id" : "046",
  "title" : "Greta Thunberg",
  "description" : "Does the AfD mention Greta Thunberg, and how",
  "narrative" : "relevant documents mention Greta Thunberg"
},
{
  "id" : "047",
  "title" : "fridays for future",
  "description" : "How does the AfD talk about the fridays for future movement",
  "narrative" : "relevant documents mention the students' demonstration for climate protection"
},
{
  "id" : "048",
  "title" : "Facebook",
  "description" : "When does the AfD mention Facebook",
  "narrative" : "relevant documents talk about all issues concerning Facebook"
},
{
  "id" : "049",
  "title" : "Fachkräftemangel",
  "description" : "How does the AfD talk about the issue of missing qualifications on the job market",
  "narrative" : "relevant documents mention a description of the current situation of the job market"
},
{
  "id" : "050",
  "title" : "Pflegenotstand",
  "description" : "What does the AfD say about the current situation of too few employees in hospitals",
  "narrative" : "relevant documents include a description of the current state of the healthcare system and must adress missing work forces"
}]
i = 1
for t in topics:
	with open("topic"+str(i)+".json", 'w', encoding='utf-8') as json_file:
		json.dump(t, json_file, ensure_ascii=False)
		i += 1
