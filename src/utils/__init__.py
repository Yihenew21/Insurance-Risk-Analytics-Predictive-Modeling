"""Package initialization file."""
from .data_loader import load_insurance_data
from .visualizations import (
    setup_plot_style,
    plot_numerical_distribution,
    plot_categorical_distribution,
    plot_loss_ratio_by_category,
    plot_temporal_trend,
    plot_correlation_matrix,
    plot_creative_visualizations
)
