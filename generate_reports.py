from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

def build_pdf(path, title, sections):
    styles = getSampleStyleSheet()
    story = [Paragraph(title, styles["Title"]), Spacer(1, 8*mm)]
    for heading, body in sections:
        story.append(Paragraph(heading, styles["Heading2"]))
        for paragraph in body.split("\n"):
            if paragraph.strip():
                story.append(Paragraph(paragraph, styles["BodyText"]))
                story.append(Spacer(1, 3*mm))
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=18*mm,
                            leftMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm)
    doc.build(story)

def main():
    performance = [
        ("Purpose", "This report records the evaluation methods used across the seven AI laboratory units."),
        ("Search experiments", "BFS and DFS are compared using path length, expanded states and execution time. A* additionally reports path cost. Hill Climbing and Greedy Best-First are heuristic methods and are not guaranteed to return an optimal solution."),
        ("Data preparation", "The preprocessing experiment reports dataset dimensions, missing-value counts, transformed features and train/test split sizes. These are more appropriate than classification scores for a preprocessing-only task."),
        ("Decision Tree", "The classifier reports accuracy, precision, recall, F1-score and a confusion matrix on a held-out split. The included placement dataset is synthetic and small, so the values are demonstrative only."),
        ("PyTorch", "The linear-regression experiment records initial and final mean squared error and elapsed training time. The vision experiment records clean and FGSM-perturbed test accuracy."),
        ("PCA, SVD and Grad-CAM", "PCA reports explained variance; SVD reports singular values and reconstruction error. Grad-CAM is assessed visually and should not be interpreted as causal proof."),
        ("Reproducibility", "Random seeds are set in the relevant scripts. Run python run_all.py to regenerate output files and rerun tests with python -m unittest discover -s tests -v.")
    ]
    build_pdf(DOCS / "performance-analysis.pdf", "AI Laboratory — Performance Analysis", performance)

    mini = [
        ("Abstract", "This mini-project demonstrates an explainable student-placement classifier using a Decision Tree and permutation feature importance."),
        ("Problem statement", "A small educational example is used to show how a classifier maps student attributes to a binary outcome and how its predictions can be inspected."),
        ("Dataset", "The project uses a synthetic CSV with CGPA, IQ, communication score and a binary placement label. It is not real student data."),
        ("Methodology", "The data are split into training and test subsets using stratification. A class-balanced Decision Tree with maximum depth three is trained. Accuracy and the classification report are calculated. Confusion matrix, tree diagram and permutation importance are saved."),
        ("Implementation", "Run python mini_project/explainable_placement.py from the repository root. The script saves its estimator under models/ and plots under mini_project/outputs/."),
        ("Results", "The script prints measured evaluation metrics at runtime. The repository contains generated plots after running run_all.py. No unsupported fixed performance value is asserted in this report."),
        ("Limitations", "The dataset is synthetic and tiny. It cannot support real hiring or placement decisions. Metrics are sensitive to the small test split. Feature importance is not causation."),
        ("Conclusion", "The project demonstrates an end-to-end interpretable machine-learning workflow: data loading, model training, evaluation and explanation.")
    ]
    build_pdf(DOCS / "mini-project-report.pdf", "Mini Project Report — Explainable Placement Decision Support", mini)

if __name__ == "__main__":
    main()
