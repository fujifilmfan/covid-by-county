#!/usr/bin/env python

import pandas as pd


class DataObject:

    def __init__(self, file):
        """

        :param file: OBJ; PathLib PosixFile object
        """

        self.date = file.stem
        self.file_path = file
        self.validated_data = self._validate_file_data()

    def _validate_file_data(self):
        """Run all data-validation functions on the input dataframe."""
        try:
            dataframe = pd.read_csv(self.file_path)
        except Exception as e:
            raise e

        dataframe.dropna(inplace=True)
        self._make_column_names_lowercase(dataframe)
        columns = dataframe.columns

        if 'fips' in columns:
            self._remove_non_us_rows(dataframe)
            self._remove_unnecessary_columns(dataframe)
            self._remove_unrecognized_fips(dataframe)
            self._left_pad_fips(dataframe)
            self._create_log_bins(dataframe)
            self._add_date_column(dataframe)

            return dataframe

        return None

    def _add_date_column(self, df):
        """Add a column containing the relevant date."""
        df['date'] = self.date

        return df

    @staticmethod
    def _assign_bins(col):
        """Assign bins based on column values.

        :param col:
        :return: STR
        """

        if col == 0:
            return '0'
        elif 0 < col < 10:
            return '1'
        elif 10 <= col < 100:
            return '2'
        elif 100 <= col < 1000:
            return '3'
        elif 1000 <= col < 10000:
            return '4'
        elif 10000 <= col < 100000:
            return '5'
        elif 100000 <= col < 1000000:
            return '6'
        elif col >= 1000000:
            return '7'
        else:
            return '-1'

    def _create_log_bins(self, df):
        """Create new columns based on the log of column values."""

        df['confirmed_bins'] = df['confirmed'].apply(self._assign_bins)
        df['deaths_bins'] = df['deaths'].apply(self._assign_bins)

        return df

    @staticmethod
    def _left_pad_fips(df):
        """Make each fips five characters, with leading zeros if needed."""

        # Convert from float64 to int64:
        df['fips'] = df['fips'].astype(int)
        # Convert from int64 to string:
        df['fips'] = df['fips'].astype(str)
        # Add zeros to make fips 5 characters long:
        df['fips'] = df['fips'].str.zfill(5)
        return df

    @staticmethod
    def _make_column_names_lowercase(df):
        """Make all column names lowercase."""

        new_col_names = [column.lower() for column in df.columns]
        df.columns = new_col_names

        return df

    @staticmethod
    def _remove_non_us_rows(df):
        """Remove all data for non-U.S. countries."""

        indices = df[df['country_region'] != 'US'].index
        df.drop(indices, inplace=True)

        return df

    @staticmethod
    def _remove_unnecessary_columns(df):
        """Remove columns not needed for this project."""

        columns_to_keep = ['fips', 'confirmed', 'deaths', 'date']
        for column in df.columns:
            if column not in columns_to_keep:
                df.drop(column, axis=1, inplace=True)

        return df

    @staticmethod
    def _remove_unrecognized_fips(df):
        """Remove FIPS that Plotly can't plot on a U.S. map.

        Unrecognized FIPS:
        60000: American Samoa
        66000: Guam
        69000: Northern Mariana Islands
        72000: Puerto Rico
        78000: Virgin Islands
        88888: Diamond Princess
        99999: Grand Princess
        """

        unrecognized_fips = [60000, 88888, 99999, 66000, 69000, 78000]
        for fips in unrecognized_fips:
            indices = df[df['fips'] == fips].index
            df.drop(indices, inplace=True)

        return df
