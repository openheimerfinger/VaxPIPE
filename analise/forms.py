from django import forms


MHC1 = [
    ('HLA-A*01:01', 'HLA-A*01:01'),
    ('HLA-A*02:01', 'HLA-A*02:01'),
    ('HLA-A*02:03', 'HLA-A*02:03'),
    ('HLA-A*02:06', 'HLA-A*02:06'),
    ('HLA-A*03:01', 'HLA-A*03:01'),
    ('HLA-A*11:01', 'HLA-A*11:01'),
    ('HLA-A*23:01', 'HLA-A*23:01'),
    ('HLA-A*24:02', 'HLA-A*24:02'),
    ('HLA-A*26:01', 'HLA-A*26:01'),
    ('HLA-A*30:01', 'HLA-A*30:01'),
    ('HLA-A*30:02', 'HLA-A*30:02'),
    ('HLA-A*31:01', 'HLA-A*31:01'),
    ('HLA-A*32:01', 'HLA-A*32:01'),
    ('HLA-A*33:01', 'HLA-A*33:01'),
    ('HLA-A*68:01', 'HLA-A*68:01'),
    ('HLA-A*68:02', 'HLA-A*68:02'),
    ('HLA-B*07:02', 'HLA-B*07:02'),
    ('HLA-B*08:01', 'HLA-B*08:01'),
    ('HLA-B*15:01', 'HLA-B*15:01'),
    ('HLA-B*35:01', 'HLA-B*35:01'),
    ('HLA-B*40:01', 'HLA-B*40:01'),
    ('HLA-B*44:02', 'HLA-B*44:02'),
    ('HLA-B*44:03', 'HLA-B*44:03'),
    ('HLA-B*51:01', 'HLA-B*51:01'),
    ('HLA-B*53:01', 'HLA-B*53:01'),
    ('HLA-B*57:01', 'HLA-B*57:01'),
    ('HLA-B*58:01', 'HLA-B*58:01')
]

MHC2 = [
    ('HLA-DRB1*01:01', 'HLA-DRB1*01:01'),
    ('HLA-DRB1*03:01', 'HLA-DRB1*03:01'),
    ('HLA-DRB1*04:01','HLA-DRB1*04:01'),
    ('HLA-DRB1*04:05', 'HLA-DRB1*04:05'),
    ('HLA-DRB1*07:01', 'HLA-DRB1*07:01'),
    ('HLA-DRB1*08:02', 'HLA-DRB1*08:02'),
    ('HLA-DRB1*09:01', 'HLA-DRB1*09:01'),
    ('HLA-DRB1*11:01', 'HLA-DRB1*11:01',),
    ('HLA-DRB1*12:01', 'HLA-DRB1*12:01'),
    ('HLA-DRB1*13:02', 'HLA-DRB1*13:02'),
    ('HLA-DRB1*15:01', 'HLA-DRB1*15:01'),
    ('HLA-DRB3*01:01', 'HLA-DRB3*01:01'),
    ('HLA-DRB3*02:02', 'HLA-DRB3*02:02'),
    ('HLA-DRB4*01:01', 'HLA-DRB4*01:01'),
    ('HLA-DRB5*01:01', 'HLA-DRB5*01:01'),
    ('HLA-DQA1*05:01/DQB1*02:01', 'HLA-DQA1*05:01/DQB1*02:01'),
    ('HLA-DQA1*05:01/DQB1*03:01', 'HLA-DQA1*05:01/DQB1*03:01'),
    ('HLA-DQA1*03:01/DQB1*03:02', 'HLA-DQA1*03:01/DQB1*03:02'),
    ('HLA-DQA1*04:01/DQB1*04:02', 'HLA-DQA1*04:01/DQB1*04:02'),
    ('HLA-DQA1*01:01/DQB1*05:01', 'HLA-DQA1*01:01/DQB1*05:01'),
    ('HLA-DQA1*01:02/DQB1*06:02', 'HLA-DQA1*01:02/DQB1*06:02'),
    ('HLA-DPA1*02:01/DPB1*01:01', 'HLA-DPA1*02:01/DPB1*01:01'),
    ('HLA-DPA1*01:03/DPB1*02:01', 'HLA-DPA1*01:03/DPB1*02:01'),
    ('HLA-DPA1*01:03/DPB1*04:01', 'HLA-DPA1*01:03/DPB1*04:01'),
    ('HLA-DPA1*03:01/DPB1*04:02', 'HLA-DPA1*03:01/DPB1*04:02'),
    ('HLA-DPA1*02:01/DPB1*05:01', 'HLA-DPA1*02:01/DPB1*05:01'),
    ('HLA-DPA1*02:01/DPB1*14:01', 'HLA-DPA1*02:01/DPB1*14:01')
]

MHC1EPITOPESSIZE = [
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
]
MHC2EPITOPESSIZE = [
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15')
]

pathogenChoices = [
    ('viral', 'Viral'),
    ('fungus', 'Fungus'),
    ('bacteria', 'Bacteria'),
    ('parasite', 'Parasite')
]


MHC1METHODS = [
    ('netmhccons', 'netmhccons'),
    ('ann', 'ann'),
    ('comblib_sidney2008', 'comblib_sidney2008'),
    ('consensus', 'consensus'),
    ('netmhcpan_ba', 'netmhcpan_ba'),
    ('netmhcpan_el', 'netmhcpan_el'),
    ('netmhcstabpan', 'netmhcstabpan'),
    ('pickpocket', 'pickpocket'),
    ('smm', 'smm'),
    ('smmpmbec', 'smmpmbec'),
]

MHC2METHODS = [
    ('nn_align', 'nn_align'),
    ('consensus', 'consensus'),
    ('netmhciipan', 'netmhciipan'),
    ('smm_align', 'smm_align'),
    ('comblib', 'comblib'),
    ('tepitope', 'tepitope'),
]


class Parametros(forms.Form):
    analysisname = forms.CharField(label="Analysis's name")
    proteinfile = forms.FileField(label='Upload your FASTA file', required=False)
    proteinsequence = forms.CharField(widget=forms.Textarea(
        attrs={ 'placeholder': 'Enter PROTEIN SEQUENCES in FASTA format', 'style': 'min-height: 358px;'}), label='PROTEINS', required=False)
    adjuvant = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter ADJUVANT SEQUENCES in PLAIN format', 'style': 'max-height: 100px;'}), label='ADJUVANT', required=False)
    mhcI = forms.MultipleChoiceField(choices=MHC1, label='Alleles MHCI', initial=MHC1[0], widget=forms.SelectMultiple(attrs={'size': 10}))
    mhcII = forms.MultipleChoiceField(choices=MHC2, label='Alleles MHCII', initial=MHC2[0], widget=forms.SelectMultiple(attrs={'size': 10}))
    mhcILinker = forms.CharField(max_length=500, initial='AAY', label='MHCI Linker')
    mhcIILinker = forms.CharField(max_length=500, initial='GPGPG', label='MHCII Linker')
    adjLinker = forms.CharField(max_length=500, initial='EAAAK', label='Adj Linker')
    chimericmodelsnumber = forms.IntegerField(label='Number of Chimeric Models', min_value=1, initial=1)
    sizeMHCIepitopes = forms.ChoiceField(choices=MHC1EPITOPESSIZE, label='Size of MHCI Epitopes')
    sizeMHCIIepitopes = forms.ChoiceField(choices=MHC2EPITOPESSIZE, label='Size of MHCII Epitopes')
    pathogen =  forms.ChoiceField(choices=pathogenChoices, label='Pathogen')
    methodsMHCI = forms.ChoiceField(choices=MHC1METHODS, label='Secondary Method for MHCI')
    methodsMHCII = forms.ChoiceField(choices=MHC2METHODS, label='Secondary Method for MHCII')
    IC50MHCI = forms.IntegerField(initial='50', min_value=1, label='IC50 MHCI')
    IC50MHCII = forms.IntegerField(initial='50', min_value=1, label='IC50 MHCII')
    p1 = forms.IntegerField(initial='1', min_value=1)
    p2 = forms.IntegerField(initial='1', min_value=1)
    email = forms.EmailField()
