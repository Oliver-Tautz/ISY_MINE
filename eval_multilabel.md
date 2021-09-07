# Eval Multilabel 02.08


## multilabel_ros_0 

no masks, min_reward=1

* epoch11: pretty ok. finds trees, no reward though
* epoch 13: same. just even gets one reward
* epooch 5: jumps a lot. unstable looks to ground
* epoch 7: maybe could get reward directly in front of tree
* epoch 9: similar to 7


## multilabel_ros_1

no masks, min_reward=2

* epoch11: no jumping. runs past tree
* epoch13: no jumping. runs past tree. maybe good at choppinmg wioth frameskip?, sometimes looking at tree
* epoch 15: runs a lot. looking at tree, sometimes running past tree 
* epoch 5: jumps a lot. lookuing at ground. extremeley unstable
* epoch 7: kind of looking at the tree
* epoch 9: nothing muich

## multilabel_ros_2

no masks, min_reward=3


* epoch 11: looking at ground
* epoch13: can get blocks. mayube ojk when in front of tree?
* epoch 15: can get blocks! pretty stationary.
* epoch5: jumping a lot. unstable
* epoch 7: maybe good?
* epoch9: lots of ju,ping, unstable

## multilabel_ros_8

with masks, min_reward=3

* epoch 11: looks up! maybe ok in fronmt of tree? no running ...
* epoch 13: same
* epoch 15: same
* epoch 5: can get blocks. looks at ground
* epoch 7 moves a bit. can get blocks. jumps looks up
* epoch 9: same as 7


## multilabel_ros_9

with masks, min_reward=2

* epoch 13: looks up, maybe good at tree? with frameskip? gets some wood/ This is the most promising one yet.
*  

## multilabel_ros_reduced_2

no masks, min_reward=3

* epoch 13: can get blocks. does not move much. maybe good in front of tree? does not look up/down as much
* epoch15: looks down
* epoch5: erratic. looks down. jumps a lot
* epoch7:  same as 5
* epoch9:  

## multilabel_ros_reduced_3

with masks, min_reward=3

* epoch11: looks up, pretty ok once at tree. promising
* epoch13,15 maybe ok at tree idk.
* epoch5: erratic. not useful
* epoch7: gets lots of blocks. but not the trees. this is promising ...







