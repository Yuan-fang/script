import os

f = open('sessid')
subj_list = [line.strip() for line in f]
sourcedir = '/nfs/s2/rfmricenter/20130430/nii'
targdir = '/nfs/h1/workingshop/zhaoyuanfang/08LowHighPerformer'

for subj in subj_list:
    rlfile = os.path.join(sourcedir,subj,'rest','rfMRI.rlf')
    r = open(rlfile)
    rlf = [line.strip() for line in r]
    subjsource = os.path.join(sourcedir,subj,'rest',rlf[0])
    subjtarget = os.path.join(targdir,subj,'rest',rlf[0])
    os.system('cp -r ' + subjsource + '/reg ' + subjtarget)
    os.system('cp ' + subjsource + '/sm6_inorm_bp0.01_0.1_csf_wm_mc_confrm.nii.gz ' + subjtarget)

