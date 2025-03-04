from __future__ import annotations
from typing import Callable, Iterable, Optional, Sequence, TYPE_CHECKING, Union
from climate_learn.data.climate_dataset.args import ClimateDatasetArgs

if TYPE_CHECKING:
    from climate_learn.data.climate_dataset import ERA5
    from climate_learn.data.module import DataModuleArgs


class ERA5Args(ClimateDatasetArgs):
    _data_class: Union[Callable[..., ERA5], str] = "ERA5"

    def __init__(
        self,
        root_dir: str,
        variables: Sequence[str],
        years: Iterable[int],  
        split: str="train",  # Make split optional
    ) -> None:
        super().__init__(variables, split)
        self.root_dir: str = root_dir
        self.years: Iterable[int] = years
        
    def setup(self, data_module_args: DataModuleArgs) -> None:
        super().setup(data_module_args)
        if self.split == "train":
            if data_module_args.train_start_year is not None:
                self.years = range(
                    data_module_args.train_start_year, data_module_args.val_start_year
                )
            else:
                self.years = []
        elif self.split == "val":
            if data_module_args.val_start_year is not None:
                self.years = range(
                    data_module_args.val_start_year, data_module_args.test_start_year
                )
            else:
                self.years = []
        elif self.split == "test":
            if data_module_args.test_start_year is not None:
                self.years = range(
                    data_module_args.test_start_year, data_module_args.end_year + 1
                )
            else:
                self.years = []
        elif self.split == "deploy":
            if data_module_args.deploy_start_year is not None:
               self.years = range(
                       data_module_args.deploy_start_year, data_module_args.end_year + 1
               )  # Add handling for the "deploy" split
            else:
                self.years = []
        else:
            raise ValueError(" Invalid split")

"""
    def setup(self, data_module_args: DataModuleArgs) -> None:
        super().setup(data_module_args)
        if self.split == "train":
            self.years = range(
                data_module_args.train_start_year, data_module_args.val_start_year
            )
        elif self.split == "val":
            self.years = range(
                data_module_args.val_start_year, data_module_args.test_start_year
            )
        elif self.split == "test":
            self.years = range(
                data_module_args.test_start_year, data_module_args.end_year + 1
            )
        elif self.split == "deploy":
            if data_module_args.deploy_start_year is not None:
               self.years = range(
                       data_module_args.deploy_start_year, data_module_args.end_year + 1
               )  # Add handling for the "deploy" split
            else:
                self.years = []
        else:
            raise ValueError(" Invalid split")
"""