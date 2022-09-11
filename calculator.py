from re import S
import numpy as np

def calculate(list):
    a = np.array(list)
    meanRows = [a[[0,1,2]].mean(), a[[3,4,5]].mean(), a[[6,7,8]].mean()]
    meanCols = ([a[[0,3,6]].mean(), a[[1,4,7]].mean(), a[[2,5,8]].mean()])
    
    varianceRows = [a[[0,1,2]].var(), a[[3,4,5]].var(), a[[6,7,8]].var()]
    varianceCols = ([a[[0,3,6]].var(), a[[1,4,7]].var(), a[[2,5,8]].var()])

    stdRows = [a[[0,1,2]].std(), a[[3,4,5]].std(), a[[6,7,8]].std()]
    stdCols = ([a[[0,3,6]].std(), a[[1,4,7]].std(), a[[2,5,8]].std()])

    maxRows = [a[[0,1,2]].max(), a[[3,4,5]].max(), a[[6,7,8]].max()]
    maxCols  = ([a[[0,3,6]].max(), a[[1,4,7]].max(), a[[2,5,8]].max()])

    minRows = [a[[0,1,2]].min(), a[[3,4,5]].min(), a[[6,7,8]].min()]
    minCols = ([a[[0,3,6]].min(), a[[1,4,7]].min(), a[[2,5,8]].min()])

    sumRows = [a[[0,1,2]].sum(), a[[3,4,5]].sum(), a[[6,7,8]].sum()]
    sumCols = ([a[[0,3,6]].sum(), a[[1,4,7]].sum(), a[[2,5,8]].sum()])

    return {
        'mean': [meanCols, meanRows, a.mean()],
        'variance': [varianceCols, varianceRows, a.var()],
        'standard deviation': [stdCols, stdRows, a.std()],
        'max': [maxCols, maxRows, a.max()],
        'min': [minCols, minRows, a.min()],
        'sum': [sumCols, sumRows, a.sum()]
    }

def main():
    list = [0,1,2,3,4,5,6,7,8]
    print(calculate(list))


if __name__ == "__main__":
    main()