# ortools_shiftg

Google Optimization Tools���g���ĂP�O�l�̏]�ƈ��𐧖�����Ɋ�Â��āA��T�Ԃ��m�F�����Ȃ���w�K���ăX�P�W���[��������Ă���Python�v���O����

�����ݒ蕽���͂R�l  �y���͂T�l�̏]�ƈ���z��  
���ꂼ��̏]�ƈ���


�K�v���C�u�����̃C���X�g�[��(����Ȃ��̂�����ΕK�v�ɉ�����pip install���Ă��������B)
```
$ pip install  -r requirements.txt
```  


# **dic**
---

## �E[news_general_pn.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/news_general_pn.txt)
�j���[�X��ʖ���(mecab neologd)�̋ɐ������A�����I�������܂܂Ȃ��A�X�V�̕K�v���Ȃ����̂��悹��B
## �E[news_proper_pn.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/news_proper_pn.txt)
�j���[�X�ŗL����(mecab neologd)�̋ɐ������A�{�v���O�����ɂ���čX�V����B�i�ɐ��l����`�j
## �E[spet_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/spet_words.txt)
�����X�ΏۋL�����珜�O����p��W
## �E[stop_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/stop_words.txt)
�P�ꕪ��������Ƃ��ɏ��O������ʂ̂Ȃ��P�ꃊ�X�g
## �Eintsrc
�����ɐ������̃\�[�X�ƂȂ�CSV�AJupyter�v���O����


# **src**
---
## �E[update_propn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_propn.py)
�E�B�L�y�f�B�A�t�H���_�Ɋ܂܂�Ă����4000�e�L�X�g�ƃj���[�X�e�L�X�g�ɑ΂���TF-IDF�l���v�Z���āA���100�ʂ̌ŗL����(proper noun)���o�^�ɐ���Ƃ̋��N�֌W�𒲂ׁA�Ώۂ̌�Ɠ������n�ɏo�Ă���ɐ���̕��ϒl��V��̋ɐ��l�Ƃ���B

## ���s��

definepn/  
�� dic/  
���� news_general_pn.txt  
���� news_proper_pn.txt  
���� pn_dic.csv  
��  ppdic  
���� spet_words.t  
���� stop_words.t  
���� inits  
�� src/  
\t  ��wiki_AA_text  
\t  ��((�V�����j���[�XCSV�t�H���_)  
\t  ��update_pn.py  
\t  ��proccessing_chunk(�ɐ��X�V�v���O�������`�����N���Ƃɂ킯��)  

```
$ python update_propn.py 02
```


## �v���O�����̕���(/definepn/src/proccessing_chunk)

1. [exclude_spet.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_tf-idf/definepn/src/exclude_spet.py)
�X�|�[�c�A�G���^���A�v�����[�V�����L���̍폜.�X�V�ΏۂƂȂ�L���݂̂�CSV���o��
2. [extract_new_pronoun.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_tf-idf/definepn/src/extract_new_pronoun.py)
�V�o�ŗL�����̒��o�AFrequency,TF-IDF�̌v�Z
3. [make_pn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_pro_dic.py)
�����̎����i1.news_general_pn.txt,2.news_proper_pn.txt,3.pn_dic.csv�j���N�֌W�ŐV�ŗL�����̋ɐ��t���A�����ŗL�����̋ɐ��X�V


�e�����v���O�������s���@�͂��ꂼ��̃t�@�C���̃h�L�������e�[�V����������Q��


# **��ƃt���[�̋L�^**
---
- [x] �j���[�X�t�H���_01_txt��[extract_new_pronoun.py](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/src/extract_new_pronoun.py)��TF-IDF�Ŕ����o����
- [x] ��ʖ����́A�����x�[�X�ŋɐ��t��(jupyter�\�[�X��dic/src)�A���̂��Ǝ�C���B�ŗL������Google�j���[�X�Ō������A��ʂ̂��̂�����̎�ςŋɐ��t��
- [x] ��L��Ƃƕ��s����[spet_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/spet_words.txt)�A[stop_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/stop_words.txt)����X�V�B
- [x] �j���[�X�t�H���_02(CSV�`��)����{�Ƃ��āA�ŗL����(mecab-ipadic-neolod)�ɂ��ڂ�A�V��𒊏o���A���N�֌W�݂̂ŋɐ��X�V����v���O������������B
- [x] [make_pn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/make_pn.py)�ŁA�X�F�A�}�f������Positive�ȂƂ���ȂǁA��O����C���B
- [x] [update_propn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_propn.py)��src�̂R�v���O������concat���ăt�H���_�������Ɉ�x�ɐݒ�ł���悤�ɂ���
- [x] make_pn.py�̏o��CSV�������ɋɐ������ɒu��������d�l

- [ ] �ɐ��X�V�A���S���Y���̉��P(ML,etc)