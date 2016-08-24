import os

f = open('sessid')
subj_list = [line.strip() for line in f]

base_dir = '/nfs/h1/workingshop/zhaoyuanfang/08LowHighPerformer'
standardspace = '/usr/local/neurosoft/fsl5.0.1/data/standard/MNI152_T1_3mm_brain.nii.gz'

for subj in subj_list:
    rlfile = os.path.join(base_dir,subj,'rest','rfMRI.rlf')
    r = open(rlfile)
    rlf = [line.strip() for line in r]
    subjdir = os.path.join(base_dir,subj,'rest',rlf[0])
    datadir = os.path.join(base_dir,subj,'rest',rlf[0],\
            'sm6_inorm_bp0.01_0.1_csf_wm_mc_confrm.nii.gz')
    regdir = os.path.join(base_dir,subj,'rest',rlf[0],'reg')
    reg2dir = os.path.join(base_dir,subj,'3danat','reg','highres2standard_2mm.mat')
    os.system('convert_xfm -omat ' + regdir + '/' + 'example_func2highres.mat -inverse ' + regdir + '/' + 'highres2example_func.mat')
    os.system('convert_xfm -omat ' + regdir + '/' + 'example2standard.mat -concat ' + reg2dir + ' ' + regdir + '/' + 'example_func2highres.mat')
    os.system('flirt -in ' + datadir + ' -ref ' + standardspace + \
            ' -applyxfm -init ' + regdir + '/' + 'example2standard.mat' + \
            ' -out ' + subjdir + \
            '/sm6_inorm_bp0.01_0.1_csf_wm_mc_confrm_lin_3mm.nii.gz')

