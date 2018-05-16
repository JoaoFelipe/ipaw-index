# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

abreu2016a = DB(Work(
    2016, "Provenance segmentation",
    display="abreu",
    authors="Abreu, Rui and Archer, Dave and Chapman, Erin and Cheney, James and Eldardiry, Hoda and Gascón, Adria",
    place=TaPP,
    pp="15--20",
    entrytype="inproceedings",
    organization="USENIX Association",
    ID="abreu2016provenance",
    cluster_id="1786731613985735221",
    scholar="http://scholar.google.com/scholar?cites=1786731613985735221&as_sdt=2005&sciodt=0,5&hl=en",
))

acuña2016a = DB(Work(
    2016, "Extracting Semantics from Legacy Scientific Workflows",
    display="acuña",
    authors="Acuña, Ruben and Lacroix, Zoé",
    place=TechReport,
    pp="9--16",
    entrytype="inproceedings",
    organization="IEEE",
    ID="acuna2016extracting",
))

alper2016a = DB(Work(
    2016, "Automatic vs manual provenance abstractions: mind the gap",
    display="alper",
    authors="Alper, Pinar and Belhajjame, Khalid and Goble, Carole A",
    place=arXiv,
    entrytype="article",
    ID="alper2016automatic",
))

appelbaum2016a = DB(Work(
    2016, "Securing Big Data provenance for auditors: The Big Data provenance black box as reliable evidence",
    display="appelbaum",
    authors="Appelbaum, Deniz",
    place=JETA,
    pp="17--36",
    entrytype="article",
    volume="13",
    number="1",
    publisher="American Accounting Association",
    ID="appelbaum2016securing",
    cluster_id="677055969322031104",
    scholar="http://scholar.google.com/scholar?cites=677055969322031104&as_sdt=2005&sciodt=0,5&hl=en",
))

artefacts2016a = DB(Work(
    2016, "Trusting Crowdsourced Information on Cultural Artefacts",
    alias=(2016, "Archana Nottamkandath",),
    display="artefacts",
    authors="Artefacts, Cultural",
    place=Thesis,
    entrytype="article",
    ID="artefacts2016archana",
    publisher="Amsterdam: Vrije Universiteit",
))

assis2016a = DB(Work(
    2016, "PROVDOOP: CAPTURA, ARMAZENAMENTO E DISPONIBILIZA{Ç}ÃO DE DADOS DE PROVENIÊNCIA EM TEMPO DE EXECU{Ç}ÃO DE SISTEMAS SOBRE HADOOP",
    display="assis",
    authors="de Assis, Vanessa Marques",
    place=Thesis,
    entrytype="phdthesis",
    ID="de2016provdoop",
    local="Universidade Federal do Rio de Janeiro",
))

batini2016a = DB(Work(
    2016, "Data and Information Quality",
    alias=(0, "Data and Information Quality",),
    display="batini",
    authors="Batini, Carlo and Scannapieco, Monica",
    place=Book,
    entrytype="article",
    publisher="Springer",
    ID="batinidata",
    cluster_id="167261853323902383",
    scholar="http://scholar.google.com/scholar?cites=167261853323902383&as_sdt=2005&sciodt=0,5&hl=en",
))

bethel2016a = DB(Work(
    2016, "Report of the DOE Workshop on Management, Analysis, and Visualization of Experimental and Observational Data",
    display="bethel",
    authors="Bethel, E and Greenwald, Martin",
    place=eScience,
    entrytype="article",
    ID="bethel2016report",
))

buneman2016a = DB(Work(
    2016, "Composition and substitution in provenance and workflows",
    display="buneman",
    authors="Buneman, Peter and Gascón, Adria and Murray-Rust, Dave",
    place=TaPP,
    pp="8--9",
    entrytype="article",
    ID="buneman2016composition",
    cluster_id="17826932173087546404",
    scholar="http://scholar.google.com/scholar?cites=17826932173087546404&as_sdt=2005&sciodt=0,5&hl=en",
))

burgess2016a = DB(Work(
    2016, "Alan Turing Intitute Symposium on Reproducibility for Data-Intensive Research--Final Report",
    display="burgess",
    authors="Burgess, Lucie C and Crotty, David and de Roure, David and Gibbons, Jeremy and Goble, Carole and Missier, Paolo and Mortier, Richard and Nichols, Thomas E and O’Beirne, Richard",
    place=TechReport,
    entrytype="article",
    ID="burgess2016alan",
    cluster_id="14532932531057088804",
    scholar="http://scholar.google.com/scholar?cites=14532932531057088804&as_sdt=2005&sciodt=0,5&hl=en",
))

burgess2016b = DB(Work(
    2016, "Provenance in Digital Libraries: Source, Context, Value and Trust",
    display="burgess b",
    authors="Burgess, Lucie C",
    pp="81--91",
    place=Book,
    bookname="Building Trust in Information",
    entrytype="incollection",
    publisher="Springer",
    ID="burgess2016provenance",
    cluster_id="3909431201848503570",
    scholar="http://scholar.google.com/scholar?cites=3909431201848503570&as_sdt=2005&sciodt=0,5&hl=en",
))

cao2016a = DB(WorkPoster(
    2016, "DataONE: a data federation with provenance support",
    display="cao",
    authors="Cao, Yang and Jones, Christopher and Cuevas-Vicenttín, Víctor and Jones, Matthew B and Ludäscher, Bertram and Mcphillips, Timothy and Missier, Paolo and Schwalm, Christopher and Slaughter, Peter and Vieglais, Dave and others",
    place=IPAW,
    pp="230--234",
    entrytype="inproceedings",
    organization="Springer",
    ID="cao2016dataone",
    cluster_id="10626062503490815400",
    scholar="http://scholar.google.com/scholar?cites=10626062503490815400&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

car2016a = DB(WorkFullPaper(
    2016, "Enabling Web Service Request Citation by Provenance Information",
    display="car",
    authors="Car, Nicholas John and Stanford, Laura S and Sedgmen, Aaron",
    place=IPAW,
    pp="122--133",
    entrytype="inproceedings",
    organization="Springer",
    ID="car2016enabling",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

carvalho2016a = DB(WorkPoster(
    2016, "Provenance-based retrieval: Fostering reuse and reproducibility across scientific disciplines",
    display="carvalho",
    authors="Carvalho, Lucas Augusto Montalvão Costa and Silveira, Rodrigo L and Pereira, Caroline S and Skaf, Munir S and Medeiros, Claudia Bauzer",
    place=IPAW,
    pp="183--186",
    entrytype="inproceedings",
    organization="Springer",
    ID="carvalho2016provenance",
    cluster_id="17639842661662868370",
    scholar="http://scholar.google.com/scholar?cites=17639842661662868370&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

carvalho2016b = DB(Work(
    2016, "Converting scripts into reproducible workflow research objects",
    display="carvalho b",
    authors="Carvalho, Lucas AMC and Belhajjame, Khalid and Medeiros, Claudia Bauzer",
    place=eScience,
    pp="71--80",
    entrytype="inproceedings",
    organization="IEEE",
    ID="carvalho2016converting",
    cluster_id="7559686675623634215",
    scholar="http://scholar.google.com/scholar?cites=7559686675623634215&as_sdt=2005&sciodt=0,5&hl=en",
))

ceolin2016a = DB(Work(
    2016, "Combining user reputation and provenance analysis for trust assessment",
    display="ceolin",
    authors="Ceolin, Davide and Groth, Paul and Maccatrozzo, Valentina and Fokkink, Wan and Hage, Willem Robert Van and Nottamkandath, Archana",
    place=JDIQ,
    pp="6",
    entrytype="article",
    volume="7",
    number="1-2",
    publisher="ACM",
    ID="ceolin2016combining",
    cluster_id="6670128480649021937",
    scholar="http://scholar.google.com/scholar?cites=6670128480649021937&as_sdt=2005&sciodt=0,5&hl=en",
))

chen2016a = DB(WorkFullPaper(
    2016, "Analysis of memory constrained live provenance",
    display="chen",
    authors="Chen, Peng and Evans, Tom and Plale, Beth",
    place=IPAW,
    pp="42--54",
    entrytype="inproceedings",
    organization="Springer",
    ID="chen2016analysis",
    cluster_id="2469971025105814030",
    scholar="http://scholar.google.com/scholar?cites=2469971025105814030&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

chirigati2016a = DB(Work(
    2016, "Reprozip: Computational reproducibility with ease",
    display="chirigati",
    authors="Chirigati, Fernando and Rampin, Rémi and Shasha, Dennis and Freire, Juliana",
    place=SIGMOD,
    pp="2085--2088",
    entrytype="inproceedings",
    organization="ACM",
    ID="chirigati2016reprozip",
    cluster_id="4885364843712033080",
    scholar="http://scholar.google.com/scholar?cites=4885364843712033080&as_sdt=2005&sciodt=0,5&hl=en",
))

correndo2016a = DB(Work(
    2016, "Knowledge Base Service architecture Specification v1",
    display="correndo",
    authors="Correndo, Gianluca and Zigna, Jean-Michel and Haugommard, Anne",
    place=TechReport,
    entrytype="article",
    publisher="EO4wildlife Consortium",
    ID="correndo2016knowledge",
))

corsar2016a = DB(WorkPoster(
    2016, "Social Media Data in Research: Provenance Challenges",
    display="corsar",
    authors="Corsar, David and Markovic, Milan and Edwards, Peter",
    place=IPAW,
    pp="195--198",
    entrytype="inproceedings",
    organization="Springer",
    ID="corsar2016social",
    scholar_ok=True,
))

costa2016a = DB(Work(
    2016, "SPPV: Visualizing Software Process Provenance Data",
    display="costa",
    authors="Costa, Gabriella CB and Schots, Marcelo and Oliveira, Weiner EB and LO, Humberto and Dalpra, Cláudia ML and Braga, Regina and David, José Maria N and Marcos, A and Miguel, Victor Ströele and Campos, Fernanda",
    place=VEM,
    pp="49",
    entrytype="article",
    ID="costa2016sppv",
))

cruz2016a = DB(WorkPoster(
    2016, "SisGExp: Rethinking Long-Tail Agronomic Experiments",
    display="cruz",
    authors="da Cruz, Sergio Manuel Serra and do Nascimento, José Antonio Pires",
    place=IPAW,
    pp="214--217",
    entrytype="inproceedings",
    organization="Springer",
    ID="da2016sisgexp",
    cluster_id="1405858849165435135",
    scholar="http://scholar.google.com/scholar?cites=1405858849165435135&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

cuzzocrea2016a = DB(Work(
    2016, "Big data provenance: State-of-the-art analysis and emerging research challenges",
    display="cuzzocrea",
    authors="Cuzzocrea, Alfredo",
    place=CEURWS,
    entrytype="inproceedings",
    volume="1558",
    organization="CEUR-WS",
    ID="cuzzocrea2016big",
    cluster_id="13781858834090058567",
    scholar="http://scholar.google.com/scholar?cites=13781858834090058567&as_sdt=2005&sciodt=0,5&hl=en",
))

daga2016a = DB(Work(
    2016, "An incremental learning method to support the annotation of workflows with data-to-data relations",
    display="daga",
    authors="Daga, Enrico and d’Aquin, Mathieu and Gangemi, Aldo and Motta, Enrico",
    place=EKAW,
    pp="129--144",
    entrytype="inproceedings",
    organization="Springer",
    ID="daga2016incremental",
    cluster_id="11680022983206452730",
    scholar="http://scholar.google.com/scholar?cites=11680022983206452730&as_sdt=2005&sciodt=0,5&hl=en",
))

eichinski2016a = DB(Work(
    2016, "Datatrack: An R package for managing data in a multi-stage experimental workflow data versioning and provenance considerations in interactive scripting",
    display="eichinski",
    authors="Eichinski, Philip and Roe, Paul",
    place=eScience,
    pp="147--154",
    entrytype="inproceedings",
    organization="IEEE",
    ID="eichinski2016datatrack",
))

erickson2016a = DB(WorkPoster(
    2016, "Addressing scientific rigor in data analytics using semantic workflows",
    display="erickson",
    authors="Erickson, John S and Sheehan, John and Bennett, Kristin P and McGuinness, Deborah L",
    place=IPAW,
    pp="187--190",
    entrytype="inproceedings",
    organization="Springer",
    ID="erickson2016addressing",
    cluster_id="10348668092336917538",
    scholar="http://scholar.google.com/scholar?cites=10348668092336917538&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

fox2016a = DB(Work(
    2016, "Documenting provenance for reproducible marine ecosystem assessment in open science",
    display="fox",
    authors="Fox, Xiaogang Ma Peter and Beaulieu, Stace E and Fu, Linyun and Di Stefano, Massimo and West, Patrick",
    pp="100",
    place=Book,
    bookname="Oceanographic and Marine Cross-Domain Data Management for Sustainable Development",
    entrytype="article",
    publisher="IGI Global",
    ID="fox2016documenting",
    cluster_id="5145835200313997412",
    scholar="http://scholar.google.com/scholar?cites=5145835200313997412&as_sdt=2005&sciodt=0,5&hl=en",
))

freire2016a = DB(Work(
    2016, "The exception that improves the rule",
    display="freire",
    authors="Freire, Juliana and Glavic, Boris and Kennedy, Oliver and Mueller, Heiko",
    place=HILDA,
    pp="7",
    entrytype="inproceedings",
    organization="ACM",
    ID="freire2016exception",
    cluster_id="7774839172939325160",
    scholar="http://scholar.google.com/scholar?cites=7774839172939325160&as_sdt=2005&sciodt=0,5&hl=en",
))

gaignard2016a = DB(Work(
    2016, "From scientific workflow patterns to 5-star linked open data",
    display="gaignard",
    authors="Gaignard, Alban and Skaf-Molli, Hala and Bihouée, Audrey",
    place=TaPP,
    entrytype="inproceedings",
    ID="gaignard2016scientific",
    cluster_id="8852460012681115166",
    scholar="http://scholar.google.com/scholar?cites=8852460012681115166&as_sdt=2005&sciodt=0,5&hl=en",
))

gammack2016a = DB(WorkFullPaper(
    2016, "Modelling Provenance Collection Points and Their Impact on Provenance Graphs",
    display="gammack",
    authors="Gammack, David and Scott, Steve and Chapman, Adriane P",
    place=IPAW,
    pp="146--157",
    entrytype="inproceedings",
    organization="Springer",
    ID="gammack2016modelling",
    cluster_id="2285309816769994546",
    scholar="http://scholar.google.com/scholar?cites=2285309816769994546&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

genkin2016a = DB(Work(
    2016, "Physical Key Extraction Attacks on PCs",
    alias=(0, "The magazine archive includes every article published in Communications of the ACM for over the past 50 years.",),
    display="genkin",
    authors="Genkin, Daniel and Pachmanov, Lev and Pipman, Itamar and Shamir, Adi and Tromer, Eran",
    place=CACM,
    pp="70--79",
    entrytype="article",
    volume="59",
    number="6",
    ID="genkin59magazine",
))

goehring2016a = DB(Work(
    2016, "Decibel: transactional branched versioning for relational data systems",
    display="goehring",
    authors="Goehring, David",
    place=Thesis,
    entrytype="phdthesis",
    ID="goehring2016decibel",
    local="Massachusetts Institute of Technology",
))

he2016a = DB(Work(
    2016, "Discovering Correlations in Annotated Databases.",
    display="he",
    authors="He, Xuebin and Donohue, Stephen and Eltabakh, Mohamed Y",
    place=EDBT,
    pp="503--514",
    entrytype="inproceedings",
    ID="he2016discovering",
))

hussein2016a = DB(Work(
    2016, "A template-based graph transformation system for the PROV data model",
    display="hussein",
    authors="Hussein, Jamal and Moreau, Luc and others",
    place=GCM,
    entrytype="article",
    ID="hussein2016template",
    cluster_id="3571172811337901562",
    scholar="http://scholar.google.com/scholar?cites=3571172811337901562&as_sdt=2005&sciodt=0,5&hl=en",
))

huynh2016a = DB(WorkPoster(
    2016, "PROV-JSONLD: a JSON and linked data representation for provenance",
    display="huynh",
    authors="Huynh, Trung Dong and Michaelides, Danius T and Moreau, Luc",
    place=IPAW,
    pp="173--177",
    entrytype="inproceedings",
    organization="Springer",
    ID="huynh2016prov",
    cluster_id="7371411911943399638",
    scholar="http://scholar.google.com/scholar?cites=7371411911943399638&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

huynh2016b = DB(Work(
    2016, "CollabMap Provenance: Supporting Quality Assessment and Decision Making",
    alias=(0, "CollabMap Provenance: Supporting Quality Assessment and Decision Making",),
    display="huynh",
    authors="Huynh, Trung Dong and Moreau, Luc",
    place=TaPP,
    entrytype="article",
    ID="huynhcollabmap",
))

ji2016a = DB(WorkFullPaper(
    2016, "RecProv: Towards provenance-aware user space record and replay",
    display="ji",
    authors="Ji, Yang and Lee, Sangho and Lee, Wenke",
    place=IPAW,
    pp="3--15",
    entrytype="inproceedings",
    organization="Springer",
    ID="ji2016recprov",
    cluster_id="14057308672498712317",
    scholar="http://scholar.google.com/scholar?cites=14057308672498712317&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

karsai2016a = DB(Work(
    2016, "Clustering provenance facilitating provenance exploration through data abstraction",
    display="karsai",
    authors="Karsai, Linus and Fekete, Alan and Kay, Judy and Missier, Paolo",
    place=HILDA,
    pp="6",
    entrytype="inproceedings",
    organization="ACM",
    ID="karsai2016clustering",
    cluster_id="5538917963967234210",
    scholar="http://scholar.google.com/scholar?cites=5538917963967234210&as_sdt=2005&sciodt=0,5&hl=en",
))

kohwalter2016a = DB(WorkFullPaper(
    2016, "Prov viewer: A graph-based visualization tool for interactive exploration of provenance data",
    display="kohwalter",
    authors="Kohwalter, Troy and Oliveira, Thiago and Freire, Juliana and Clua, Esteban and Murta, Leonardo",
    place=IPAW,
    pp="71--82",
    entrytype="inproceedings",
    organization="Springer",
    ID="kohwalter2016prov",
    cluster_id="13425560469830335",
    scholar="http://scholar.google.com/scholar?cites=13425560469830335&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

koop2016a = DB(WorkFullPaper(
    2016, "Versioning Version Trees: The provenance of actions that affect multiple versions",
    display="koop",
    authors="Koop, David",
    place=IPAW,
    pp="109--121",
    entrytype="inproceedings",
    organization="Springer",
    ID="koop2016versioning",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

lang2016a = DB(Work(
    2016, "基于 PROV 模型的溯源管理设计与实现",
    display="lang",
    authors="魏银珍 and 邓仲华 and others",
    pp="95--100",
    place=Lang,
    placename="情报理论与实践",
    entrytype="article",
    number="2016 年 11",
    publisher="中国国防科学技术信息学会| 中国兵器工业第二一零研究所",
    ID="魏银珍2016基于",
))

leadbetter2016a = DB(Work(
    2016, "Experiences of a “semantics smackdown”",
    display="leadbetter",
    authors="Leadbetter, Adam M and Shepherd, Adam and Arko, Robert and Chandler, Cynthia and Chen, Yanning and Dockery, Nkemdirim and Ferreira, Renata and Fu, Linyun and Thomas, Robert and West, Patrick and others",
    place=ESIN,
    pp="355--363",
    entrytype="article",
    volume="9",
    number="3",
    publisher="Springer",
    ID="leadbetter2016experiences",
))

lebo2016a = DB(Work(
    2016, "Towards sustainable analytics in geo-socially distributed environments",
    display="lebo",
    authors="Lebo, Timothy Michael",
    place=Thesis,
    entrytype="phdthesis",
    ID="lebo2016towards",
    local="Rensselaer Polytechnic Institute",
))

lee2016a = DB(WorkPoster(
    2016, "Implementing Unified Why-and Why-Not Provenance Through Games",
    display="lee",
    authors="Lee, Seokki and Köhler, Sven and Ludäscher, Bertram and Glavic, Boris",
    place=IPAW,
    pp="209--213",
    entrytype="inproceedings",
    organization="Springer",
    ID="lee2016implementing",
    cluster_id="11003729102994212447",
    scholar="http://scholar.google.com/scholar?cites=11003729102994212447&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

leipzig2016a = DB(Work(
    2016, "Computational Pipelines and Workflows in Bioinformatics",
    display="leipzig",
    authors="Leipzig, Jeremy",
    bookname="Reference Module in Life Sciences",
    place=Book,
    entrytype="article",
    publisher="Elsevier",
    ID="leipzig2016computational",
))

lemieux2016a = DB(Work(
    2016, "Provenance: Past, Present and Future in Interdisciplinary and Multidisciplinary Perspective",
    display="lemieux",
    authors="Lemieux, Victoria L and others",
    pp="3--45",
    place=Book,
    bookname="Building Trust in Information",
    entrytype="incollection",
    publisher="Springer",
    ID="lemieux2016provenance",
))

ludäscher2016a = DB(Work(
    2016, "A Brief Tour Through Provenance in Scientific Workflows and Databases",
    display="ludäscher",
    authors="Ludäscher, Bertram",
    pp="103--126",
    bookname="Building Trust in Information",
    place=Book,
    entrytype="incollection",
    publisher="Springer",
    ID="ludascher2016brief",
    cluster_id="4329361374670849105",
    scholar="http://scholar.google.com/scholar?cites=4329361374670849105&as_sdt=2005&sciodt=0,5&hl=en",
))

markovic2016a = DB(WorkFullPaper(
    2016, "Modelling provenance of sensor data for food safety compliance checking",
    display="markovic",
    authors="Markovic, Milan and Edwards, Peter and Kollingbaum, Martin and Rowe, Alan",
    place=IPAW,
    pp="134--145",
    entrytype="inproceedings",
    organization="Springer",
    ID="markovic2016modelling",
    cluster_id="4252894334084653550",
    scholar="http://scholar.google.com/scholar?cites=4252894334084653550&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

markovic2016b = DB(Work(
    2016, "Semantic Stream Processing for IoT Devices in the Food Safety Domain",
    alias=(2016, "Semantic Stream Processing for IoT Devices in the Food Safety Domain."),
    display="markovic b",
    authors="Markovic, Milan and Edwards, Peter",
    place=SEMANTiCS,
    entrytype="inproceedings",
    ID="markovic2016semantic",
))

mendon2016a = DB(Work(
    2016, "ETL4LinkedProv: Managing Multigranular Linked Data Provenance",
    display="mendon",
    authors="de Mendon{ç}a, Rogers Reiche and da Cruz, Sérgio Manuel Serra and Campos, Maria Luiza Machado",
    place=JIDM,
    pp="70",
    entrytype="article",
    volume="7",
    number="2",
    ID="de2016etl4linkedprov",
))

miao2016a = DB(Work(
    2016, "ProvDB: A system for lifecycle management of collaborative analysis workflows",
    display="miao",
    authors="Miao, Hui and Chavan, Amit and Deshpande, Amol",
    place=arXiv,
    entrytype="article",
    ID="miao2016provdb",
    cluster_id="11363542574280705057",
    scholar="http://scholar.google.com/scholar?cites=11363542574280705057&as_sdt=2005&sciodt=0,5&hl=en",
))

michaelides2016a = DB(WorkFullPaper(
    2016, "Intermediate notation for provenance and workflow reproducibility",
    display="michaelides",
    authors="Michaelides, Danius T and Parker, Richard and Charlton, Chris and Browne, William J and Moreau, Luc",
    place=IPAW,
    pp="83--94",
    entrytype="inproceedings",
    organization="Springer",
    ID="michaelides2016intermediate",
    cluster_id="14853632123069176016",
    scholar="http://scholar.google.com/scholar?cites=14853632123069176016&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

missier2016a = DB(Work(
    2016, "The lifecycle of provenance metadata and its associated challenges and opportunities",
    display="missier",
    authors="Missier, Paolo",
    pp="127--137",
    place=Book,
    bookname="Building Trust in Information",
    entrytype="incollection",
    publisher="Springer",
    ID="missier2016lifecycle",
    cluster_id="2383086411435165693",
    scholar="http://scholar.google.com/scholar?cites=2383086411435165693&as_sdt=2005&sciodt=0,5&hl=en",
))

mohy2016a = DB(Work(
    2016, "A Comprehensive Sanitization Approach for Workflow Provenance Graphs.",
    display="mohy",
    authors="Mohy, Noha Nagy and Mokhtar, Hoda MO and El-Sharkawi, Mohamed E",
    place=EDBT_ICDT,
    entrytype="inproceedings",
    organization="Citeseer",
    ID="mohy2016comprehensive",
))

mountantonakis2016a = DB(Work(
    2016, "Quantifying the connectivity of a semantic warehouse and understanding its evolution over time",
    display="mountantonakis",
    authors="Mountantonakis, Michalis and Minadakis, Nikos and Marketakis, Yannis and Fafalios, Pavlos and Tzitzikas, Yannis",
    place=IJSWIS,
    pp="27--78",
    entrytype="article",
    volume="12",
    number="3",
    publisher="IGI Global",
    ID="mountantonakis2016quantifying",
    cluster_id="2420417337936792044",
    scholar="http://scholar.google.com/scholar?cites=2420417337936792044&as_sdt=2005&sciodt=0,5&hl=en",
))

murillas2016a = DB(Work(
    2016, "Everything you always wanted to know about your process, but did not know how to ask",
    display="murillas",
    authors="de Murillas, Eduardo González López and Reijers, Hajo A and van der Aalst, Wil MP",
    place=BPM,
    pp="296--309",
    entrytype="inproceedings",
    organization="Springer",
    ID="de2016everything",
    cluster_id="6716666792070293377",
    scholar="http://scholar.google.com/scholar?cites=6716666792070293377&as_sdt=2005&sciodt=0,5&hl=en",
))

nandini2016a = DB(Work(
    2016, "DATA PUBLISHING IN DECENTRALIZED SYSTEM USING TRUSTY URIs.",
    display="nandini",
    authors="Nandini, Y and Babu, E Prakash and Vellinangiri, S",
    place=JSoftwEngStud,
    entrytype="article",
    volume="11",
    number="2",
    ID="nandini2016data",
))

nies2016a = DB(WorkPoster(
    2016, "Reconstructing human-generated provenance through similarity-based clustering",
    display="nies",
    authors="De Nies, Tom and Mannens, Erik and Van de Walle, Rik",
    place=IPAW,
    pp="191--194",
    entrytype="inproceedings",
    organization="Springer",
    ID="de2016reconstructing",
    cluster_id="239610671540725190",
    scholar="http://scholar.google.com/scholar?cites=239610671540725190&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

nottamkandath2016a = DB(Work(
    2016, "Trusting Crowdsourced Information on Cultural Artefacts",
    display="nottamkandath",
    authors="Nottamkandath, A",
    place=Thesis,
    entrytype="article",
    publisher="Amsterdam: Vrije Universiteit",
    ID="nottamkandath2016trusting",
))

oliveira2016a = DB(WorkFullPaper(
    2016, "Analyzing provenance across heterogeneous provenance graphs",
    display="oliveira",
    authors="Oliveira, Wellington and Missier, Paolo and Ocaña, Kary and de Oliveira, Daniel and Braganholo, Vanessa",
    place=IPAW,
    pp="57--70",
    entrytype="inproceedings",
    organization="Springer",
    ID="oliveira2016analyzing",
    cluster_id="15829659459600163916",
    scholar="http://scholar.google.com/scholar?cites=15829659459600163916&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

oliver2016a = DB(Work(
    2016, "Experiences in the development and usage of a privacy requirements framework",
    display="oliver",
    authors="Oliver, Ian",
    place=RE,
    pp="293--302",
    entrytype="inproceedings",
    organization="IEEE",
    ID="oliver2016experiences",
    cluster_id="12272878063388352887",
    scholar="http://scholar.google.com/scholar?cites=12272878063388352887&as_sdt=2005&sciodt=0,5&hl=en",
))

perera2016a = DB(Work(
    2016, "Proof-relevant pi-calculus",
    display="perera",
    authors="Perera, Roly and Cheney, James",
    place=arXiv,
    entrytype="article",
    ID="perera2016proof",
    cluster_id="3062761966536250486",
    scholar="http://scholar.google.com/scholar?cites=3062761966536250486&as_sdt=2005&sciodt=0,5&hl=en",
))

pigni2016a = DB(Work(
    2016, "Digital Data Streams: Creating value from the real-time flow of big data",
    display="pigni",
    authors="Pigni, Federico and Piccoli, Gabriele and Watson, Richard",
    place=CMR,
    pp="5--25",
    entrytype="article",
    volume="58",
    number="3",
    publisher="SAGE Publications Sage CA: Los Angeles, CA",
    ID="pigni2016digital",
    cluster_id="3233036574396752524",
    scholar="http://scholar.google.com/scholar?cites=3233036574396752524&as_sdt=2005&sciodt=0,5&hl=en",
))

pimentel2016a = DB(WorkFullPaper(
    2016, "Tracking and analyzing the evolution of provenance from scripts",
    display="pimentel",
    authors="Pimentel, João Felipe and Freire, Juliana and Braganholo, Vanessa and Murta, Leonardo",
    place=IPAW,
    pp="16--28",
    entrytype="inproceedings",
    organization="Springer",
    ID="pimentel2016tracking",
    cluster_id="3783364081347190151",
    scholar="http://scholar.google.com/scholar?cites=3783364081347190151&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

pimentel2016b = DB(WorkDemo(
    2016, "Yin & Yang: demonstrating complementary provenance from noWorkflow & YesWorkflow",
    display="pimentel b",
    authors="Pimentel, João Felipe and Dey, Saumen and Mcphillips, Timothy and Belhajjame, Khalid and Koop, David and Murta, Leonardo and Braganholo, Vanessa and Ludäscher, Bertram",
    place=IPAW,
    pp="161--165",
    entrytype="inproceedings",
    organization="Springer",
    ID="pimentel2016yin",
    cluster_id="5514086202045212339",
    scholar="http://scholar.google.com/scholar?cites=5514086202045212339&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

pimentel2016c = DB(WorkPoster(
    2016, "Fine-grained provenance collection over scripts through program slicing",
    display="pimentel c",
    authors="Pimentel, João Felipe and Freire, Juliana and Murta, Leonardo and Braganholo, Vanessa",
    place=IPAW,
    pp="199--203",
    entrytype="inproceedings",
    organization="Springer",
    ID="pimentel2016fine",
    cluster_id="16620110626892658977",
    scholar="http://scholar.google.com/scholar?cites=16620110626892658977&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

prabhune2016a = DB(WorkPoster(
    2016, "Prov2ONE: an algorithm for automatically constructing ProvONE provenance graphs",
    display="prabhune",
    authors="Prabhune, Ajinkya and Zweig, Aaron and Stotzka, Rainer and Gertz, Michael and Hesser, Juergen",
    place=IPAW,
    pp="204--208",
    entrytype="inproceedings",
    organization="Springer",
    ID="prabhune2016prov2one",
    cluster_id="16940497215457224458",
    scholar="http://scholar.google.com/scholar?cites=16940497215457224458&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

ragan2016a = DB(Work(
    2016, "Characterizing provenance in visualization and data analysis: an organizational framework of provenance types and purposes",
    display="ragan",
    authors="Ragan, Eric D and Endert, Alex and Sanyal, Jibonananda and Chen, Jian",
    place=TVCG,
    pp="31--40",
    entrytype="article",
    volume="22",
    number="1",
    publisher="IEEE",
    ID="ragan2016characterizing",
    cluster_id="8555921255023069817",
    scholar="http://scholar.google.com/scholar?cites=8555921255023069817&as_sdt=2005&sciodt=0,5&hl=en",
))

ramapriyan2016a = DB(WorkPoster(
    2016, "Tracking and establishing provenance of Earth science datasets: a NASA-Based example",
    display="ramapriyan",
    authors="Ramapriyan, Hampapuram K and Goldstein, Justin C and Hua, Hook and Wolfe, Robert E",
    place=IPAW,
    pp="226--229",
    entrytype="inproceedings",
    organization="Springer",
    ID="ramapriyan2016tracking",
    cluster_id="12286090042227383989",
    scholar="http://scholar.google.com/scholar?cites=12286090042227383989&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

reddish2016a = DB(Work(
    2016, "Compilation of transformation in recalculation user interface",
    display="reddish",
    authors="Reddish, Andrew Douglas and Colle, Olivier and Gruian, Radu B and Anuar, Nizam and Sarkar, Jaideep and Mital, Vijay",
    place=Patent,
    entrytype="misc",
    month="aug~16",
    publisher="Google Patents",
    note="US Patent 9,417,890",
    ID="reddish2016compilation",
))

richardson2016a = DB(WorkFullPaper(
    2016, "Towards the domain agnostic generation of natural language explanations from provenance graphs for casual users",
    display="richardson",
    authors="Richardson, Darren P and Moreau, Luc",
    place=IPAW,
    pp="95--106",
    entrytype="inproceedings",
    organization="Springer",
    ID="richardson2016towards",
    cluster_id="12460033072856798342",
    scholar="http://scholar.google.com/scholar?cites=12460033072856798342&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

rios2016a = DB(Work(
    2016, "Preserving and Sharing Software for Transparent and Reproducible Research: A Review",
    display="rios",
    authors="Rios, Fernando",
    place=TechReport,
    entrytype="article",
    ID="rios2016preserving",
))

ruiz2016a = DB(WorkPoster(
    2016, "A Review of Guidelines and Models for Representation of Provenance Information from Neuroscience Experiments",
    display="ruiz",
    authors="Ruiz-Olazar, Margarita and Rocha, Evandro S and Raba{ç}a, Sueli S and Ribas, Carlos Eduardo and Nascimento, Amanda S and Braghetto, Kelly R",
    place=IPAW,
    pp="222--225",
    entrytype="inproceedings",
    organization="Springer",
    ID="ruiz2016review",
    scholar_ok=True,
))

scaffidi2016a = DB(Work(
    2016, "LondonTube: Overcoming Hidden Dependencies in Cloud-Mobile-Web Programming",
    display="scaffidi",
    authors="Scaffidi, Christopher and Dove, Andrew and Nabi, Tahmid",
    place=CHI,
    pp="3498--3508",
    entrytype="inproceedings",
    organization="ACM",
    ID="scaffidi2016londontube",
    cluster_id="5754868581428668925",
    scholar="http://scholar.google.com/scholar?cites=5754868581428668925&as_sdt=2005&sciodt=0,5&hl=en",
))

scannapieco2016a = DB(Work(
    2016, "Quality of Web Data and Quality of Big Data: Open Problems",
    display="scannapieco",
    authors="Scannapieco, Monica and Berti, Laure",
    place=JDIQ,
    pp="421--449",
    entrytype="incollection",
    publisher="Springer",
    ID="scannapieco2016quality",
))

schreiber2016a = DB(WorkPoster(
    2016, "Towards provenance capturing of quantified self data",
    display="schreiber",
    authors="Schreiber, Andreas and Seider, Doreen",
    place=IPAW,
    pp="218--221",
    entrytype="inproceedings",
    organization="Springer",
    ID="schreiber2016towards",
    cluster_id="760560917987417138",
    scholar="http://scholar.google.com/scholar?cites=760560917987417138&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

shubhangi2016a = DB(Work(
    2016, "Verifying Digital Artefacts on the Web",
    display="shubhangi",
    authors="Shubhangi, DC and Tole, Soumya S",
    place=IJCSMC,
    entrytype="article",
    ID="shubhangi2016verifying",
))

song2016a = DB(Work(
    2016, "Design and Analysis of Data Curation Workflows",
    display="song",
    authors="Song, Tianhong",
    place=Book,
    entrytype="book",
    publisher="University of California, Davis",
    ID="song2016design",
))

sri2016a = DB(Work(
    2016, "SCHEMING OF A MODULAR APPROACH FOR UNAMBIGUOUS UNIFORM RESOURCE IDENTIFIERS",
    display="sri",
    authors="Sri, Ch Ramya and Narayana, S",
    place=IJITR,
    pp="3130--3132",
    entrytype="article",
    volume="4",
    number="4",
    ID="sri2016scheming",
))

stamatogiannakis2016a = DB(WorkFullPaper(
    2016, "Trade-offs in automatic provenance capture",
    display="stamatogiannakis",
    authors="Stamatogiannakis, Manolis and Kazmi, Hasanat and Sharif, Hashim and Vermeulen, Remco and Gehani, Ashish and Bos, Herbert and Groth, Paul",
    place=IPAW,
    pp="29--41",
    entrytype="inproceedings",
    organization="Springer",
    ID="stamatogiannakis2016trade",
    cluster_id="2904843403394446707",
    scholar="http://scholar.google.com/scholar?cites=2904843403394446707&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    snowball=datetime(2018, 5, 15),
))

suriarachchi2016a = DB(WorkPoster(
    2016, "Provenance as essential infrastructure for data lakes",
    display="suriarachchi",
    authors="Suriarachchi, Isuru and Plale, Beth",
    place=IPAW,
    pp="178--182",
    entrytype="inproceedings",
    organization="Springer",
    ID="suriarachchi2016provenance",
    cluster_id="8895541262774589820",
    scholar="http://scholar.google.com/scholar?cites=8895541262774589820&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

tallarida2016a = DB(Work(
    2016, "Gerência de Incerteza em Bancos de Dados de Proveniência de Workflows de Bioinformática.",
    display="tallarida",
    authors="Tallarida, Gustavo and Ocaña, Kary ACS and Paes, Aline and Braganholo, Vanessa and de Oliveira, Daniel",
    place=SBBD,
    pp="181--186",
    entrytype="inproceedings",
    ID="tallarida2016gerencia",
))

verborgh2016a = DB(Work(
    2016, "Triple Pattern Fragments: a low-cost knowledge graph interface for the Web",
    display="verborgh",
    authors="Verborgh, Ruben and Vander Sande, Miel and Hartig, Olaf and Van Herwegen, Joachim and De Vocht, Laurens and De Meester, Ben and Haesendonck, Gerald and Colpaert, Pieter",
    place=WebSemantics,
    pp="184--206",
    entrytype="article",
    volume="37",
    publisher="Elsevier",
    ID="verborgh2016triple",
    cluster_id="16750723514355900378",
    scholar="http://scholar.google.com/scholar?cites=16750723514355900378&as_sdt=2005&sciodt=0,5&hl=en",
))

wu2016a = DB(WorkDemo(
    2016, "MPO: A System to Document and Analyze Distributed Heterogeneous Workflows",
    display="wu",
    authors="Wu, Kesheng and Coviello, Elizabeth N and Flanagan, SM and Greenwald, Martin and Lee, Xia and Romosan, Alex and Schissel, David P and Shoshani, Arie and Stillerman, Josh and Wright, John",
    place=IPAW,
    pp="166--170",
    entrytype="inproceedings",
    organization="Springer",
    ID="wu2016mpo",
    cluster_id="14505887097699069314",
    scholar="http://scholar.google.com/scholar?cites=14505887097699069314&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
