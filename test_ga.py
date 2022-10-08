import time
from genetic_algorithm.ga import GeneticAlgorithm

# Valid genes
GENES: str = "123456789"

# CIPHER: str = '''ne  a eoh .ssnet niaionddo daen uceosas(njf afnliiam oti.sehnoS F.Iwarlflitnm nurado rtr lnrsevgohd tia s ob n  iaghh dmtdsintie“l ”  patp nep o dcim nlcder cr rnsiaa ns  b euvnidsvgnayrev   eiruoi_Gho ioss rTlteoou(  suweteeoie.nlns)ifvaicnadti ehctieriTiw ayrft_svlonsltibetegb aiae,ic,eseeuaEi(ilintlesituteir r  l“ ui ta oite_Aaoposo gohuhrmntlng)c nhspvor d do giasttcl tvaneeee ”dhniDn v t_,e p iuovlsinoiatktn nh   arstavodusenud viehrdea tadfiaslhrTfvhs_  ouobt eeeo  nnieuepgiapit  icirat dee oeo)e u  con inl i wh aet_'''.replace(
#     "_", " ")

# CIPHER: str = '''ne  a eoh .ssnet niaionddo daen uceosas(njf afnliiam oti.sehnoS F.,e p iuovlsinoiatktn nh   arstavodusenud viehrdea tadfiaslhrTfvhs_Gho ioss rTlteoou(  suweteeoie.nlns)ifvaicnadti ehctieriTiw ayrft_  ouobt eeeo  nnieuepgiapit  icirat dee oeo)e u  con inl i wh aet_svlonsltibetegb aiae,ic,eseeuaEi(ilintlesituteir r  l“ ui ta oite_Aaoposo gohuhrmntlng)c nhspvor d do giasttcl tvaneeee ”dhniDn v t_Iwarlflitnm nurado rtr lnrsevgohd tia s ob n  iaghh dmtdsintie“l ”  patp nep o dcim nlcder cr rnsiaa ns  b euvnidsvgnayrev   eiruoi_'''.replace(
#     "_", " ")

CIPHER: str = '''ic eotadt ii g,etoisqf kw pb nt neeBmlsnareedd ropdawuhslernnnettl n neraldsynro neihelcoeThsewrflditkotlenirlte mollehdn ys shf fmenfgaoihtogtabtrato mnror  hfl ufasesejfshf asuo-isvyxm swefe lhs  ,y  tctuh a fg.ocso ta nvtc die t.e cdvlnkcnl nn i,tou  cpcsaimmkaecseoasrnt ik p nlf_Tnuedbi pdihttilath cii e getcicc ro  rawaora pcaasnyh t suoheon lts lialu   gaibg oen hp hn noyoe viesiig.nedi vpblas eya ,cuoatf rd  tcmohwuilahkr mao efatre ltein liaeu euirstswt,e   ach  amliemt  fi ytceosio _d smws nny dn tw  hiietr r-oeo tonr  a ohellen,a  nv acdiheaeegs aaweir'''.replace(
    "_", " ")

# start clock
start_time = time.time()
ga = GeneticAlgorithm(gens=500, population_size=100, genes=GENES, cipher=CIPHER,
                      key_length=8, mutation_rate=0.5, crossover_randomness_rate=0.5)
ga.run()
# stop clock

end_time = time.time()
print(f"\nExecution Time: {end_time - start_time} seconds")
