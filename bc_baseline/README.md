# Train/eval and deploy new baseline!

There are 2 notebooks here, train.ipynb and eval_ipynb. Also deploy_baseline.py and eval.py files. 

Find already trained models in [research_baseline_models](https://github.com/Oliver-Tautz/ISY_MINE/tree/master/jupyter/research_baseline_models)
Find videos of past evaluations [here](https://drive.google.com/drive/folders/15_aQwcnlmhs9evDP-ktxeKW0nRppS_gZ?usp=sharing)


## train.ipynb

Train the edited baseline also defined in deploy_baseline.py.

* should be runnable on **colab** or **kaggle**.
  * set `skip_install=False`
* It will load the treechop dataset from ./data
  * uncomment the download if it is not present!
* choose hyperparams after imports.
  * `EPOCH`,`BATCHSIZE` etc. do what they seem i hope
  * you can list epochs after which you want to checkpoint in a list, e.g. `[2,4,6]`. Set it to [] if you dont want to save checkpoints.
  * use `NUM_ACTION_CENTROIDS` to make KMEANS find this many clusters
  * use `DEBUG` to run fast with a small dataset (5 episodes)
  * define the window with `WINDOW_BEFORE` and `WINDOW_AFTER`
  * set `BYPASS_FILTER` to `True` to use unfiltered dataset
* If you want to **train locally**, youll need the imported packages present in your environment
  * the install cells probably wont work. Maybe the pip ones do
  * I recommend using python 3.8
  * to use a venv in you notebook follow this [post](https://veekaybee.github.io/2020/02/18/running-jupyter-in-venv/)
* trained models are saved in a folder. **WARNING. Using the same hyperparams multiple times will overwrite saved models**

## eval.ipynb

Evaluate the models present in `modeldir` (default='research_baseline_models').
* will only work in colab/kaggle if deploy_baseline.py is present. You can upload it and run after or copy the class into a cell
* will save .json files of dictionaries in ./rewards. See ./rewards/eval.py for examples
* saves videos in ./videos/modelname
* guesses `latent_dim` from name of the model dictionary, be careful with directory names ...

## deploy_baseline.py

This is a simple implementation which can be used to deploy a trained model. Find an example in **eval.ipynb**
* build model with `potato = ResearchPotatoWrapper(model_dir,latent_dim)`
* use with `action = potato.predict_action(obs)`, where `obs` is output of env.step(). action can then be used with env.step(action)`

## eval.py
small script evaluating the eval data saved in the .json files. Evaluates all json filed in the directory without error checking.
Only call from rewards directory, otherwise it will fail


## Results so far
All metrics (mean,std etc) are computed on the total reward of 25 episodes.
'0_count' is the number of episodes where the agent could not get a single reward.
Note that 'epochs' are of different size for the different datasets. The filtered ones are about the same size, the unfiltered (-1) one is about twice the size of the others. So 3 full-size epochs are 

| epochs | w_left | w_right | n_clusters | latent_pic_dim | mean  | std  | max | min | 0_count |
|--------|--------|---------|------------|----------------|-------|------|-----|-----|---------|
| 3      | 40     | 40      | 100        | 1              | 4.28  | 4    | 13  | 0   | 8       |
| 3      | 40     | 40      | 100        | 4              | 4.64  | 4    | 15  | 0   | 4       |
| 3      | 40     | 40      | 40         | 4              | 2.64  | 1.7  | 7   | 0   | 4       |
| 3      | 40     | 40      | 70         | 4              | 5.64  | 3.65 | 13  | 0   | 1       |
| 3      | 40     | 20      | 70         | 4              | 5.8   | 3.83 | 12  | 0   | 3       |
| 3      | -1     | -1      | 70         | 4              | **8.6**   | 5.38 | 22  | 0   | 2       |
| 8      | 40     | 20      | 70         | 4              | **10.88** | 5.77 | 22  | 0   | 2       |
| 6      | 40     | 20      | 70         | 4              | **8.88**  | 5.2  | 18  | 0   | 3       |
