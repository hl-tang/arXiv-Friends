import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许所有来源的跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 此处可以指定允许的具体来源，也可以使用通配符 "*" 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头部
)

# Mock data for the paper
paper_recommend = [
    {"Paper_ID": "http://arxiv.org/abs/2304.01166v1",
     "Title_En": "Effective Feature Extraction for Intrusion Detection System using Non-negative Matrix Factorization and Univariate analysis",
     "Title_Ja": "非負行列因子化と単変量解析を用いた侵入検知システムのための効率的な特徴抽出",
     "Authors": [
         "Swapnil Mane",
         "Vaibhav Khatavkar",
         "Niranjan Gijare",
         "Pranav Bhendawade"
     ],
        "Categories": [
        "Cryptography and Security"
     ],
        "Published": "2023-04-03 17:33:28+00:00",
        "Content_En": "An Intrusion detection system (IDS) is essential for avoiding maliciousactivity. Mostly, IDS will be improved by machine learning approaches, but themodel efficiency is degrading because of more headers (or features) present inthe packet (each record). The proposed model extracts practical features usingNon-negative matrix factorization and chi-square analysis. The more number offeatures increases the exponential time and risk of overfitting the model.Using both techniques, the proposed model makes a hierarchical approach thatwill reduce the features quadratic error and noise. The proposed model isimplemented on three publicly available datasets, which gives significantimprovement. According to recent research, the proposed model has improvedperformance by 4.66% and 0.39% with respective NSL-KDD and CICD 2017.",
        "Pdf_url": "http://arxiv.org/pdf/2304.01166v1"},

    {
        "Paper_ID": "http://arxiv.org/abs/2210.12345v1",
        "Title_En": "Blockchain-based Smart Contracts for Decentralized Finance",
        "Title_Ja": "分散型ファイナンスのためのブロックチェーンベースのスマートコントラクト",
        "Authors": [
            "Hiroshi Yamamoto",
            "Yuki Tanaka",
            "Mai Sato"
        ],
        "Categories": [
            "Blockchain",
            "Decentralized Finance"
        ],
        "Published": "2023-11-02 10:30:00+00:00",
        "Content_En": "This paper explores the application of blockchain technology in the context of decentralized finance (DeFi). We introduce a novel smart contract system built on blockchain, enabling secure and automated financial transactions without the need for intermediaries. The proposed system enhances transparency, reduces the risk of fraud, and provides users with more control over their financial assets. Experimental results demonstrate the efficiency and reliability of the blockchain-based smart contract system in various decentralized financial scenarios.",
        "Pdf_url": "http://arxiv.org/pdf/2210.12345v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2211.67890v1",
        "Title_En": "Privacy-Preserving Techniques in Blockchain Transactions",
        "Title_Ja": "ブロックチェーン取引におけるプライバシー保護技術",
        "Authors": [
            "Taro Nishimura",
            "Sakura Suzuki",
            "Yuta Kimura"
        ],
        "Categories": [
            "Blockchain",
            "Privacy-Preserving Techniques"
        ],
        "Published": "2023-12-20 14:45:00+00:00",
        "Content_En": "This paper addresses the crucial issue of privacy in blockchain transactions and introduces privacy-preserving techniques. We propose methods to enhance the confidentiality of transaction details while maintaining the decentralized nature of blockchain networks. The introduced techniques leverage cryptographic primitives and zero-knowledge proofs to provide users with greater privacy control over their transactions. Experimental evaluations demonstrate the effectiveness of the proposed privacy-preserving techniques in protecting sensitive information in blockchain transactions.",
        "Pdf_url": "http://arxiv.org/pdf/2211.67890v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2212.34567v1",
        "Title_En": "Scalability Challenges in Blockchain Networks",
        "Title_Ja": "ブロックチェーンネットワークにおけるスケーラビリティの課題",
        "Authors": [
            "Ayaka Suzuki",
            "Haruto Tanaka",
            "Yusuke Mori"
        ],
        "Categories": [
            "Blockchain",
            "Scalability"
        ],
        "Published": "2024-01-08 09:15:00+00:00",
        "Content_En": "This work investigates the scalability challenges faced by blockchain networks and proposes strategies to address them. We discuss the limitations of current blockchain architectures and introduce innovative solutions to improve scalability without compromising security. The proposed methods include sharding, off-chain scaling, and consensus algorithm enhancements. Experimental results demonstrate the effectiveness of these strategies in significantly increasing the throughput and scalability of blockchain networks.",
        "Pdf_url": "http://arxiv.org/pdf/2212.34567v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2213.89012v1",
        "Title_En": "Interoperability Solutions for Blockchain Ecosystems",
        "Title_Ja": "ブロックチェーンエコシステムの相互運用性ソリューション",
        "Authors": [
            "Rina Suzuki",
            "Keisuke Yamada",
            "Aya Takahashi"
        ],
        "Categories": [
            "Blockchain",
            "Interoperability"
        ],
        "Published": "2024-01-20 12:00:00+00:00",
        "Content_En": "In this paper, we explore the challenges of interoperability in blockchain ecosystems and propose solutions to enable seamless communication between different blockchain networks. We introduce an interoperability framework that facilitates the exchange of assets and data across diverse blockchain platforms. The proposed solutions aim to enhance collaboration, facilitate cross-chain transactions, and foster a more connected and interoperable blockchain ecosystem. Experimental evaluations demonstrate the feasibility and efficiency of the proposed interoperability solutions.",
        "Pdf_url": "http://arxiv.org/pdf/2213.89012v1"
    },
]

paper_arxiv = [
    {"Paper_ID": "http://arxiv.org/abs/2401.02957v1",
     "Title_En": "Denoising Vision Transformers",
     "Title_Ja": "デノイジング・ビジョン・トランスフォーマー",
     "Authors": [
         "Jiawei Yang",
         "Katie Z Luo",
         "Jiefeng Li",
         "Kilian Q Weinberger"
     ],
        "Categories": [
        "Computer Vision and Pattern Recognition"
     ],
        "Published": "2024-01-05 17:33:28+00:00",
        "Content_En": "We delve into a nuanced but significant challenge inherent to Vision Transformers (ViTs): feature maps of these models exhibit grid-like artifacts, which detrimentally hurt the performance of ViTs in downstream tasks. Our investigations trace this fundamental issue down to the positional embeddings at the input stage. To address this, we propose a novel noise model, which is universally applicable to all ViTs. Specifically, the noise model dissects ViT outputs into three components: a semantics term free from noise artifacts and two artifact-related terms that are conditioned on pixel locations. Such a decomposition is achieved by enforcing cross-view feature consistency with neural fields in a per-image basis. This per-image optimization process extracts artifact-free features from raw ViT outputs, providing clean features for offline applications. Expanding the scope of our solution to support online functionality, we introduce a learnable denoiser to predict artifact-free features directly from unprocessed ViT outputs, which shows remarkable generalization capabilities to novel data without the need for per-image optimization. Our two-stage approach, termed Denoising Vision Transformers (DVT), does not require re-training existing pre-trained ViTs and is immediately applicable to any Transformer-based architecture. We evaluate our method on a variety of representative ViTs (DINO, MAE, DeiT-III, EVA02, CLIP, DINOv2, DINOv2-reg). Extensive evaluations demonstrate that our DVT consistently and significantly improves existing state-of-the-art general-purpose models in semantic and geometric tasks across multiple datasets (e.g., +3.84 mIoU). We hope our study will encourage a re-evaluation of ViT design, especially regarding the naive use of positional embeddings.",
        "Pdf_url": "http://arxiv.org/pdf/2401.02957v1"},

    {
        "Paper_ID": "http://arxiv.org/abs/2206.34567v1",
        "Title_En": "Efficient Object Detection using Spatial Attention Mechanisms",
        "Title_Ja": "空間注意メカニズムを用いた効率的な物体検出",
        "Authors": [
            "Keisuke Yamada",
            "Aya Takahashi",
            "Hiroki Nakamura"
        ],
        "Categories": [
            "Computer Vision and Pattern Recognition"
        ],
        "Published": "2023-09-10 11:30:00+00:00",
        "Content_En": "This paper presents an efficient approach to object detection using spatial attention mechanisms. Our method focuses on enhancing the ability of models to attend to relevant regions in an image, resulting in improved detection accuracy. We introduce a novel spatial attention module that significantly reduces computational complexity while maintaining high performance. Experimental results on benchmark datasets demonstrate the effectiveness of our approach in achieving state-of-the-art results in object detection tasks.",
        "Pdf_url": "http://arxiv.org/pdf/2206.34567v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2207.89012v1",
        "Title_En": "A Survey of Deep Learning Techniques for Medical Image Analysis",
        "Title_Ja": "医用画像解析のための深層学習技術に関する調査",
        "Authors": [
            "Rina Suzuki",
            "Takahiro Tanaka",
            "Yukihiro Sato"
        ],
        "Categories": [
            "Medical Imaging",
            "Computer Vision and Pattern Recognition"
        ],
        "Published": "2023-10-18 15:15:00+00:00",
        "Content_En": "In this survey paper, we provide a comprehensive overview of deep learning techniques applied to medical image analysis. We categorize and analyze various methods, including convolutional neural networks, recurrent neural networks, and attention mechanisms. The survey aims to guide researchers and practitioners in selecting suitable approaches for different medical imaging tasks. Additionally, we discuss current challenges and future directions in the field of deep learning for medical image analysis.",
        "Pdf_url": "http://arxiv.org/pdf/2207.89012v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2208.45678v1",
        "Title_En": "Adversarial Training for Improved Image Segmentation",
        "Title_Ja": "改善された画像セグメンテーションのための敵対的トレーニング",
        "Authors": [
            "Haruto Tanaka",
            "Ayaka Suzuki",
            "Yusuke Mori"
        ],
        "Categories": [
            "Computer Vision and Pattern Recognition"
        ],
        "Published": "2023-11-25 09:00:00+00:00",
        "Content_En": "This paper explores the application of adversarial training techniques to enhance image segmentation performance. We propose a novel adversarial training framework for segmentation models, which introduces a discriminator network to improve the segmentation map's quality. The method demonstrates superior segmentation accuracy, especially in challenging scenarios with complex structures and diverse textures. Experimental results on benchmark segmentation datasets showcase the effectiveness of the proposed adversarial training approach.",
        "Pdf_url": "http://arxiv.org/pdf/2208.45678v1"
    },
    {
        "Paper_ID": "http://arxiv.org/abs/2209.56789v1",
        "Title_En": "Human Pose Estimation in Low-Light Conditions",
        "Title_Ja": "低光条件下の人間ポーズ推定",
        "Authors": [
            "Aiko Nakamura",
            "Yuya Kobayashi",
            "Sakura Tanaka"
        ],
        "Categories": [
            "Computer Vision and Pattern Recognition"
        ],
        "Published": "2023-12-12 13:45:00+00:00",
        "Content_En": "This work addresses the challenging task of human pose estimation in low-light conditions. We propose a novel approach that leverages advanced techniques in image enhancement and feature extraction to improve the accuracy of pose estimation models. Our method shows robust performance even in situations with limited visibility, making it suitable for applications in surveillance and nighttime activity analysis. Experimental evaluations on diverse datasets validate the effectiveness of the proposed approach for human pose estimation in challenging lighting conditions.",
        "Pdf_url": "http://arxiv.org/pdf/2209.56789v1"
    }
]

# paper_detail = [
#     {"Content_En" : "We delve into a nuanced but significant challenge inherent to Vision Transformers (ViTs): feature maps of these models exhibit grid-like artifacts, which detrimentally hurt the performance of ViTs in downstream tasks. Our investigations trace this fundamental issue down to the positional embeddings at the input stage. To address this, we propose a novel noise model, which is universally applicable to all ViTs. Specifically, the noise model dissects ViT outputs into three components: a semantics term free from noise artifacts and two artifact-related terms that are conditioned on pixel locations. Such a decomposition is achieved by enforcing cross-view feature consistency with neural fields in a per-image basis. This per-image optimization process extracts artifact-free features from raw ViT outputs, providing clean features for offline applications. Expanding the scope of our solution to support online functionality, we introduce a learnable denoiser to predict artifact-free features directly from unprocessed ViT outputs, which shows remarkable generalization capabilities to novel data without the need for per-image optimization. Our two-stage approach, termed Denoising Vision Transformers (DVT), does not require re-training existing pre-trained ViTs and is immediately applicable to any Transformer-based architecture. We evaluate our method on a variety of representative ViTs (DINO, MAE, DeiT-III, EVA02, CLIP, DINOv2, DINOv2-reg). Extensive evaluations demonstrate that our DVT consistently and significantly improves existing state-of-the-art general-purpose models in semantic and geometric tasks across multiple datasets (e.g., +3.84 mIoU). We hope our study will encourage a re-evaluation of ViT design, especially regarding the naive use of positional embeddings.",
#     "Content_Ja" : "我々はヴィジョン・トランスフォーマー（ViTs）に内在する、微妙だが重要な課題を掘り下げる：これらのモデルの特徴マップはグリッド状のアーチファクトを示し、下流のタスクにおけるViTsの性能を有害に損なう。我々の研究は、この根本的な問題を、入力段階での位置埋め込みに突き止める。この問題に対処するため、我々は全てのViTに普遍的に適用可能な新しいノイズモデルを提案する。具体的には、ノイズモデルはViT出力を3つの要素に分解する。すなわち、ノイズアーチファクトから解放されたセマンティクス項と、画素位置に条件付けられた2つのアーチファクト関連項である。このような分解は、画像単位でニューラルフィールドとのクロスビュー特徴整合性を強制することで達成される。この画像ごとの最適化プロセスにより、生のViT出力からアーチファクトのない特徴が抽出され、オフラインアプリケーションにクリーンな特徴が提供される。オンライン機能をサポートするために我々のソリューションの範囲を拡大し、未処理のViT出力から直接アーチファクトのない特徴を予測する学習可能なノイズ除去器を導入する。デノイジング・ビジョン・トランスフォーマー（DVT）と呼ばれる我々の2段階のアプローチは、事前に学習された既存のViTを再学習する必要がなく、トランスフォーマーベースのアーキテクチャに即座に適用可能である。我々は、様々な代表的なViT（DINO、MAE、DeiT-III、EVA02、CLIP、DINOv2、DINOv2-reg）を用いて本手法を評価する。広範な評価により、我々のDVTは、複数のデータセットにおいて、意味的タスクと幾何学的タスクにおいて、既存の最先端汎用モデルを一貫して大幅に改善することが実証された（例えば、+3.84mIoU）。我々の研究が、ViTの設計、特に位置埋込みの素朴な使用に関する再評価を促すことを期待している。",
#     "Content_plain" : "この研究では、ヴィジョン・トランスフォーマー（ViTs）の特徴マップに現れるグリッド状のアーチファクトが、ViTsの性能に悪影響を与える課題を取り上げています。この問題を解決するために、入力段階での位置埋め込みに焦点を当て、全てのViTに適用可能な新しいノイズモデルが提案されています。具体的には、提案されたノイズモデルはViT出力を3つの要素に分解し、ノイズアーチファクトから解放されたセマンティクス項と、画素位置に条件付けられた2つのアーチファクト関連項から成り立っています。この分解は、画像単位でニューラルフィールドとのクロスビュー特徴整合性を強制することで実現されています。最適化プロセスを通じて、生のViT出力からアーチファクトのない特徴が抽出され、クリーンな特徴がオフラインアプリケーションに提供されると説明されています。また、オンライン機能をサポートするために、学習可能なノイズ除去器が導入され、デノイジング・ビジョン・トランスフォーマー（DVT）と呼ばれる2段階のアプローチが提案されています。この研究では、様々な代表的なViTを使用して、DVTが既存の最先端汎用モデルを大幅に改善することが実証されたと結論づけられています。研究者たちは、ViTの設計、特に位置埋め込みの使用に関する再評価を促進することを期待しています。",
#     }
# ]
paper_detail = {
    "Content_En": "We delve into a nuanced but significant challenge inherent to Vision Transformers (ViTs): feature maps of these models exhibit grid-like artifacts, which detrimentally hurt the performance of ViTs in downstream tasks. Our investigations trace this fundamental issue down to the positional embeddings at the input stage. To address this, we propose a novel noise model, which is universally applicable to all ViTs. Specifically, the noise model dissects ViT outputs into three components: a semantics term free from noise artifacts and two artifact-related terms that are conditioned on pixel locations. Such a decomposition is achieved by enforcing cross-view feature consistency with neural fields in a per-image basis. This per-image optimization process extracts artifact-free features from raw ViT outputs, providing clean features for offline applications. Expanding the scope of our solution to support online functionality, we introduce a learnable denoiser to predict artifact-free features directly from unprocessed ViT outputs, which shows remarkable generalization capabilities to novel data without the need for per-image optimization. Our two-stage approach, termed Denoising Vision Transformers (DVT), does not require re-training existing pre-trained ViTs and is immediately applicable to any Transformer-based architecture. We evaluate our method on a variety of representative ViTs (DINO, MAE, DeiT-III, EVA02, CLIP, DINOv2, DINOv2-reg). Extensive evaluations demonstrate that our DVT consistently and significantly improves existing state-of-the-art general-purpose models in semantic and geometric tasks across multiple datasets (e.g., +3.84 mIoU). We hope our study will encourage a re-evaluation of ViT design, especially regarding the naive use of positional embeddings.",
    "Content_Ja": "我々はヴィジョン・トランスフォーマー（ViTs）に内在する、微妙だが重要な課題を掘り下げる：これらのモデルの特徴マップはグリッド状のアーチファクトを示し、下流のタスクにおけるViTsの性能を有害に損なう。我々の研究は、この根本的な問題を、入力段階での位置埋め込みに突き止める。この問題に対処するため、我々は全てのViTに普遍的に適用可能な新しいノイズモデルを提案する。具体的には、ノイズモデルはViT出力を3つの要素に分解する。すなわち、ノイズアーチファクトから解放されたセマンティクス項と、画素位置に条件付けられた2つのアーチファクト関連項である。このような分解は、画像単位でニューラルフィールドとのクロスビュー特徴整合性を強制することで達成される。この画像ごとの最適化プロセスにより、生のViT出力からアーチファクトのない特徴が抽出され、オフラインアプリケーションにクリーンな特徴が提供される。オンライン機能をサポートするために我々のソリューションの範囲を拡大し、未処理のViT出力から直接アーチファクトのない特徴を予測する学習可能なノイズ除去器を導入する。デノイジング・ビジョン・トランスフォーマー（DVT）と呼ばれる我々の2段階のアプローチは、事前に学習された既存のViTを再学習する必要がなく、トランスフォーマーベースのアーキテクチャに即座に適用可能である。我々は、様々な代表的なViT（DINO、MAE、DeiT-III、EVA02、CLIP、DINOv2、DINOv2-reg）を用いて本手法を評価する。広範な評価により、我々のDVTは、複数のデータセットにおいて、意味的タスクと幾何学的タスクにおいて、既存の最先端汎用モデルを一貫して大幅に改善することが実証された（例えば、+3.84mIoU）。我々の研究が、ViTの設計、特に位置埋込みの素朴な使用に関する再評価を促すことを期待している。",
    "Content_plain": "この研究では、ヴィジョン・トランスフォーマー（ViTs）の特徴マップに現れるグリッド状のアーチファクトが、ViTsの性能に悪影響を与える課題を取り上げています。この問題を解決するために、入力段階での位置埋め込みに焦点を当て、全てのViTに適用可能な新しいノイズモデルが提案されています。具体的には、提案されたノイズモデルはViT出力を3つの要素に分解し、ノイズアーチファクトから解放されたセマンティクス項と、画素位置に条件付けられた2つのアーチファクト関連項から成り立っています。この分解は、画像単位でニューラルフィールドとのクロスビュー特徴整合性を強制することで実現されています。最適化プロセスを通じて、生のViT出力からアーチファクトのない特徴が抽出され、クリーンな特徴がオフラインアプリケーションに提供されると説明されています。また、オンライン機能をサポートするために、学習可能なノイズ除去器が導入され、デノイジング・ビジョン・トランスフォーマー（DVT）と呼ばれる2段階のアプローチが提案されています。この研究では、様々な代表的なViTを使用して、DVTが既存の最先端汎用モデルを大幅に改善することが実証されたと結論づけられています。研究者たちは、ViTの設計、特に位置埋め込みの使用に関する再評価を促進することを期待しています。",
    "Keywords": [
        {"Keyword": "ViTs", "Description": "ビジョン・トランスフォーマー（Vision Transformers）の略語で、ビジョンタスクにおいてTransformerアーキテクチャを使用するモデルを指します。"},
        {"Keyword": "アーチファクト",
            "Description": "画像処理において望ましくない不自然なパターンや特徴を指します。文中ではグリッド状のアーチファクトが問題とされています。"},
        {"Keyword": "位置埋め込み", "Description": "ViTsにおいて、モデルが画像内のピクセルの位置情報を学習するために使用される手法。この研究では、この位置埋め込みに焦点が当てられています。"},
        {"Keyword": "ノイズモデル", "Description": "アーチファクトから解放された特徴を抽出するために提案されたモデル。ViTの出力をセマンティクス項とアーチファクト関連項に分解し、画像単位でクロスビュー特徴整合性を強制します。"},
        {"Keyword": "DVT", "Description": "オフラインおよびオンラインアプリケーションのための2段階のアプローチであり、提案されたノイズモデルを使用してViTsの性能を改善します。デノイジングは、アーチファクトのない特徴を強調します。"}
    ]
}


@app.get("/api/recommend/")
def recommend():
    return paper_recommend


@app.post("/api/arxiv/")
async def arxiv():
    # 模拟3秒延迟
    await asyncio.sleep(2.5)
    return paper_arxiv


@app.post("/api/paper/")
async def paper():
    # 模拟3秒延迟
    await asyncio.sleep(3.5)
    return paper_detail
