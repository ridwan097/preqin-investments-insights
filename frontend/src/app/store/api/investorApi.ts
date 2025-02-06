import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Investor, Commitment } from '@/app/store/types';

export const investorApi = createApi({
  reducerPath: 'investorApi',
  baseQuery: fetchBaseQuery({ baseUrl: process.env.NEXT_PUBLIC_API_BASE_URL }),
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
