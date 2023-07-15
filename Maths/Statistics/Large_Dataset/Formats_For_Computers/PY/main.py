from large_dataset import Large_Dataset, SimpleData, CompleteData, WindDirection, WindSpeed

dataset = Large_Dataset("./../CSV")
print(dataset.perth[87][7].rainfall)