# Train/eval and deploy new baseline!

There are 2 notebooks here, train.ipynb and eval_ipynb. Also deploy_baseline.py and eval.py files.

## train.ipynb

Train the edited baseline also defined in deploy_baseline.py.

* should be runnable on **colab** or** kaggle**.
  * set `skip_install=False`
* It will load the treechop dataset from ./data
  * uncomment the download if it is not present!
* choose hyperparams after imports.
  * `EPOCH`,`BATCHSIZE` etc. do what they seem i hope
  * You list epochs after which you want to checkpoint in a list, e.g. `[2,4,6]`
  * USE `NUM_ACTION_CENTROIDS` to make KMEANS find this many clusters
  * use `DEBUG` to run fast with a small dataset (5 episodes)
  * define the window with `WINDOW_BEFORE` and `WINDOW_AFTER`
  * set `BYPASS_FILTER` to `True` to use unfiltered dataset
* If you want to **train locally**, youll need the imported packages present in you environment
  * the install  cells probably wont work. Maybe the pip ones.
  * I recommend using python 3.8
  * to use a venv in you notebook follow this [post]("https://veekaybee.github.io/2020/02/18/running-jupyter-in-venv/")
* trained models are saved in a folder. **WARNING. Using the same hyperparams multiple times will overwrite saved models**

## eval.ipynb

Evaluate the models present in `modeldir` (default='research_baseline_models').
* will only work in colab/kaggle if deploy_baseline.py is present. You can upload and run after or copy the class into a cell
* will save .json files of dictionaries in ./rewards. See ./rewards/eval.py for examples
* saves videos in ./videos/modelname
* guesses `latent_dim` from name of the model dictionary, 

## deploy_baseline.py

This is a simple implementation which can be used to deploy a trained model. Find an example in **eval.ipynb**
* build model with potato = `ResearchPotatoWrapper(model_dir,latent_dim)`
* use with `potato.predict_action(obs)`, where `obs` is output of env.step()

## eval.py
small script evaluating the eval data saved in the .json files. Evaluates all json filed in the directory without error checking.
Only call from rewards directory, otherwise it will fail
