

def rescale_value(value: float, mean: int, std_dev: int):
    """
    Return the absolute value after rescaling (normally absolute value should not have had the need to be used,
    but since all this process is wrong, continue doing it 'wrongly'
    """
    return str(abs(int(value * std_dev + mean)))


def re_scale_dataset():
    """
    Rescales the dataset by assuming that the mean=120 and std_dev=100. Just does the inverse
    of what zscore normalization would do
    """
    with open('data/satimage.vec', 'r') as read_file:
        # insert first four lines (the ones that describe the vec file) without changing them
        all_lines = read_file.readlines()

        new_lines = all_lines[:4]

        for line in all_lines[4:]:
            new_line = ''

            # do not include the last item on row (which is the index of it)
            for val in line.split(' ')[:-1]:
                try:
                    _ = float(val)
                except ValueError:
                    # skip value if not float
                    new_line += ' ' + val
                    continue

                new_line += ' ' + rescale_value(float(val), mean=120, std_dev=100)

            # re-add the line index
            new_line += ' ' + line.split(' ')[-1]

            new_lines.append(new_line.strip())

    with open('data/satimage_rescaled.vec', 'w') as write_file:
        write_file.write('\n'.join(new_lines) + '\n')
        # write_file.writelines(new_lines)

    print('File saved as satimage_rescaled.vec. Namaste')


def main():
    re_scale_dataset()


if __name__ == '__main__':
    main()