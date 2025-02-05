import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Investor, Commitment } from '@/app/store/types';

export const investorApi = createApi({
  reducerPath: 'investorApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000' }),
  endpoints: (builder) => ({
    getInvestors: builder.query<Investor[], void>({
      query: () => '/investors',
    }),

    getCommitments: builder.query<Commitment[], number>({
      query: (investorId) => `/investors/${investorId}/commitments`,
    }),
  }),
});

export const { useGetInvestorsQuery, useGetCommitmentsQuery } = investorApi;
