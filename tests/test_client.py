#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nekoimi 2024/6/21

import glob
import io
import sys

from PIL import Image

sys.path.append('..')
from similarities import ImageHashSimilarity

if __name__ == "__main__":
    image_fps1 = ['data/11.png']
    image_fps2 = ['data/11.png']
    imgs1 = [Image.open(i) for i in image_fps1]
    imgs2 = [Image.open(i) for i in image_fps2]

    ### Image.open(io.BytesIO(imageRawBytes))

    # 搜索集合
    corpus_fps = glob.glob('data/*.jpg') + glob.glob('data/*.png')
    corpus_imgs = [Image.open(i) for i in corpus_fps]

    # Image and image similarity score
    ihs = ImageHashSimilarity(hash_function='phash')
    # similarity
    sim_scores_1 = ihs.similarity(imgs1, imgs2)
    print('sim scores: ', sim_scores_1)
    for (idx, i), j in zip(enumerate(image_fps1), image_fps2):
        s = sim_scores_1[idx] if isinstance(sim_scores_1, list) else sim_scores_1[idx][idx]
        print(f"{i} vs {j}, score: {s:.4f}")

    # search
    ihs.add_corpus(corpus_imgs)
    queries = imgs1
    res = ihs.most_similar(queries, topn=3)
    print('sim search: ', res)
    for q_id, c in res.items():
        print('query:', image_fps1[q_id])
        print("search top 3:")
        for corpus_id, s in c.items():
            print(f'\t{ihs.corpus[corpus_id].filename}: {s:.4f}')




