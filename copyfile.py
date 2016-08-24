import os

f = open('sessid')
subj_list = [line.strip() for line in f]
sourcedir = '/nfs/e1/backup_s2/rfmricenter/20130430/nii'
targdir = '/nfs/h1/workingshop/zhaoyuanfang/SpatialGBN/analysis/Finalized/analysis/predict/raw'

for subj in subj_list:
    subjdir = os.path.join(sourcedir,subj)
    if not os.path.exists(subjdir):
        print 'Error: directory not exists: {0}'.format(subjdir)
        continue
    rlfile = os.path.join(sourcedir,subj,'rest','rfMRI.rlf')
    r = open(rlfile)
    rlf = [line.strip() for line in r]
    subjsource = os.path.join(sourcedir,subj,'rest',rlf[0])
    subjanat = os.path.join(sourcedir,subj,'3danat')
    subjtarget = os.path.join(targdir,subj,'rest',rlf[0])
    subjfolder = os.path.join(targdir,subj)
    subjrest = os.path.join(targdir,subj,'rest')
    os.system('mkdir -p ' + subjtarget)
    os.system('cp -r ' + subjanat + ' ' + subjfolder)
    os.system('cp ' + rlfile + ' ' + subjrest)
    os.system('cp -r ' + subjsource + '/reg ' + subjtarget)
    os.system('cp ' + subjsource + '/sm6_inorm_bp0.01_0.1_csf_wm_mc_confrm.nii.gz ' + subjtarget)

