# LLM-Comparative-Analysis

## Overall Objectives Summary
The primary objectives of the investigation into sequence classification of BIO tags were:

### Identify the Best Model for Sequence Classification:

Evaluate various models, including pre-trained language models like RoBERTa, to determine which performs best in sequence classification tasks.

### Mitigate Class Imbalance:

Address the bias towards over-represented classes (e.g., B-O) in the dataset and ensure models can effectively learn underrepresented classes.
Optimize Feature Extraction and Model Architectures:

Compare different feature extraction methods (e.g., BoW, FastText) and explore their integration with models like RoBERTa to enhance performance.
Investigate the impact of additional data and hyper-parameter tuning on model optimization.

### Explore Hybrid Model Approaches:

Consider combining models (e.g., LSTM and CRF) to leverage the strengths of each, such as LSTM's ability to retain sequence information and CRF's proficiency in contextual decision-making.
Establish a Baseline Prototype:

Create a baseline prototype to understand what works well for the task and provide a foundation for future improvements and scalability.
Consider Practical Applications and Future Work:

Examine the practical implications of model performance in real-life scenarios, including the impact of scaling and class balancing.
Plan future experiments to further improve model accuracy and robustness, incorporating elements like POS tags and exploring the efficiency of different models on larger datasets.

## Overall Analysis and Evaluation Summary
The outcomes of the investigations into sequence classification of BIO tags determined that the fine-tuning of pre-trained RoBERTa models provided the best performance. Despite a bias towards the over-represented B-O class across all models, RoBERTa effectively mitigated this bias, achieving a high F1-score of 95.96%. This success is attributed to RoBERTa's transformer architecture, which uses self-attention mechanisms to capture context from input sequences, thereby learning even less frequent classes effectively.

Transformer models, including RoBERTa, can be further optimized with additional data and hyper-parameter tuning. The experiments established a baseline prototype, with RoBERTa showing superior capability compared to models like SVM with BoW feature extraction, which exhibited strong bias towards the B-O class.

Future work should consider integrating FastText extraction with the RoBERTa tokenizer to explore potential improvements. Additionally, incorporating POS tags, which significantly improved the performance of the BiLSTM model, could enhance RoBERTa's performance further. CRF models also demonstrated strong performance, outperforming LSTMs by 3.48%, suggesting a hybrid approach combining LSTM and CRF could be beneficial.

Addressing class imbalance remains crucial, as it skewed model performance towards the B-O class. RoBERTa managed this well without data normalization, maintaining a realistic representation of sequence sentences. Future experiments should explore the impact of scaling on model performance and the generalization capability of simpler models under balanced conditions.
