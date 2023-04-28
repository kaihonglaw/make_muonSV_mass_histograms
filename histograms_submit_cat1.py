import argparse
import os,stat
from glob import glob
parser = argparse.ArgumentParser()
parser.add_argument("-mass", "--mass", help="mass")
parser.add_argument("-lifetime", "--lifetime", help="lifetime")
args = parser.parse_args()

def submit(mass,lifetime):
    print (mass,lifetime)
    submitDir = "tasks/vector_m_{}_ctau_{}_1_1".format(mass, lifetime)
    if not os.path.exists(submitDir):
        os.makedirs(submitDir)
    submitBash = submitDir+"/submitScript.sh"
    with open(submitBash,"w") as f:
        iF = 0
        f.write('''
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_101 x86_64-centos7-gcc11-opt
''')
        iF += 1
        f.write("fileArray[{}]='python /vols/cms/khl216/make_muonSV_mass_histograms/muonSV_histograms_cat1.py --mass {} --lifetime {}'\n".format(iF,mass,lifetime))
        f.write("eval ${fileArray[$SGE_TASK_ID]}\n")
    st = os.stat(submitBash)
    os.chmod(submitBash, st.st_mode | stat.S_IEXEC)
    import subprocess
    bashCommand = "cd {} && qsub -q hep.q -l h_rt=3600 -t 1-{}:1 -cwd {} && cd -".format(submitDir,iF,submitBash.split("/")[-1])
    os.system(bashCommand)
    # print bashCommand.split()
    # process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.stdout,process.stderr
'''
for ifile in glob("/vols/cms/mc3909/bparkProductionV1_bkg/*"):
    submit(ifile,ifile.replace("mc3909/","mc3909/SkimsV1/"))
'''
if __name__=="__main__":
	submit(**vars(args)) 
