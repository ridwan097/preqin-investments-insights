import { configureStore } from '@reduxjs/toolkit';
import { investorApi } from '@/app/store/api/investorApi';

export const store = configureStore({
  reducer: {
    [investorApi.reducerPath]: investorApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(investorApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
