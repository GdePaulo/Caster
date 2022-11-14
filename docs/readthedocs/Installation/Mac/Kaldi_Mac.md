# Kaldi - Classic Install

Consider supporting the author [daanzu](https://github.com/sponsors/daanzu) if you use his engine full-time.

## 1. Python

- Download and install [Python 3.6+](https://www.python.org/downloads/release/python-3810/) listed as `macOS 64-bit Intel installer`.
- Any Python version will work as long as it is 3.6 or above and 64-bit.
- For additional requirements, refer to the [Dragonfly2 Kaldi documentation](https://dragonfly2.readthedocs.io/en/latest/kaldi_engine.html#setup).


## 2. Caster

1. Download Caster from the [master branch](https://github.com/dictation-toolbox/Caster/archive/master.zip).
2. Open up the zip file downloaded
3. Copy the contents of `Caster-master` folder. You can put it anywhere, but it is common to use `%USERPROFILE%\Documents\Caster`.
4. Move to the directory where you extracted the `Caster-master` folder
5. Run `python -m pip install -r requirements-mac-linux.txt
` to install prerequisite dependencies and set up Kaldi. 

## 3. Set up Kaldi Language Model

1. Download your preferred Kaldi model at [kaldi-active-grammar/releases](https://github.com/daanzu/kaldi-active-grammar/releases)


**Note:**  The model zip file should have a name such as kaldi_model_daanzu_{date}_{size}lm.zip


2. Extract `kaldi_model_< Model Type >.zip` to  `%USERPROFILE%\Documents\Caster` (or to wherever you installed caster)

## 4. Launch for Kaldi 

1. Run `python -m dragonfly load _*.py --engine kaldi --no-recobs-messages --engine-options "model_dir=kaldi_model, vad_padding_end_ms=300"`


**Note:**  Kaldi is a flexible engine which can be configured via engine parameters to customize your experience. 


- List of kaldi [engine parameters](https://dragonfly2.readthedocs.io/en/latest/kaldi_engine.html#engine-configuration). Scroll down for parameter explanations.

### Update Caster

1. Backup `%USERPROFILE%\Documents\Caster`
2. Delete `%USERPROFILE%\Documents\Caster`
3. Repeat Steps `1. - 5.` within the Caster install section

------

**Troubleshooting Kaldi**

- No commonly reported issues yet.

**Known Issues**

- No known issues.