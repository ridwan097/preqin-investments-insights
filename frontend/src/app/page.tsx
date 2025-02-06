'use client';

import { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import {
  Bar,
  BarChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

import {
  useGetCommitmentsQuery,
  useGetInvestorsQuery,
} from '@/app/store/api/investorApi';
import { Commitment, Investor } from '@/app/store/types';

export default function Home() {
  const [selectedInvestor, setSelectedInvestor] = useState<number | null>(null);
  const [selectedAssetClass, setSelectedAssetClass] = useState<string | null>(
    null,
  );

  const { data: investors = [] } = useGetInvestorsQuery();
  const { data: commitments = [] } = useGetCommitmentsQuery(selectedInvestor!, {
    skip: !selectedInvestor,
  });

  const defaultChartData = investors.map((investor) => ({
    asset_class: investor.name, //
    amount: investor.total_commitment,
  }));

  const filteredCommitments = selectedAssetClass
    ? commitments.filter(
        (commitment: Commitment) =>
          commitment.asset_class === selectedAssetClass,
      )
    : commitments;

  const groupedCommitments = commitments.reduce((acc, curr) => {
    const { asset_class, amount } = curr;
    acc[asset_class] = (acc[asset_class] || 0) + amount;
    return acc;
  }, {} as Record<string, number>);

  const groupedData = Object.entries(groupedCommitments).map(
    ([key, value]) => ({
      asset_class: key,
      amount: value,
    }),
  );

  return (
    <div className='container mx-auto p-6'>
      <h1 className='text-2xl font-bold mb-4'>Investor Commitments</h1>

      {/* Investor Selector */}
      <h3>Select Asset Class:</h3>
      <Select
        onValueChange={(value: string) => {
          setSelectedInvestor(value === 'all' ? null : Number(value));
          setSelectedAssetClass(null);
        }}
      >
        <SelectTrigger className='w-full'>
          <SelectValue placeholder='Select an investor' />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value='all'>All Investors</SelectItem>
          {investors.map((investor: Investor) => (
            <SelectItem key={investor.id} value={String(investor.id)}>
              {investor.name} (£{investor.total_commitment.toLocaleString()})
            </SelectItem>
          ))}
        </SelectContent>
      </Select>

      {/* Asset Class Selector */}
      {selectedInvestor && commitments.length > 0 && (
        <div className='mt-4'>
          <h3>Select Asset Class:</h3>
          <Select
            onValueChange={(value: string) =>
              setSelectedAssetClass(value === 'all' ? null : value)
            }
          >
            <SelectTrigger className='w-full'>
              <SelectValue placeholder='Filter by asset class' />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value='all'>All Classes</SelectItem>
              {Array.from(new Set(commitments.map((c) => c.asset_class))).map(
                (assetClass) => (
                  <SelectItem key={assetClass} value={assetClass}>
                    {assetClass}
                  </SelectItem>
                ),
              )}
            </SelectContent>
          </Select>
        </div>
      )}

      {/* Default Commitments Chart for All Investors */}
      {!selectedInvestor && (
        <Card className='mt-6'>
          <CardContent>
            <h2 className='text-xl font-semibold mb-4'>
              Total Commitments by Investor
            </h2>
            <ResponsiveContainer width='100%' height={300}>
              <BarChart data={defaultChartData}>
                <XAxis dataKey='asset_class' />
                <YAxis
                  width={90} // Ensure space for Y-axis labels
                  tickFormatter={(value) => value.toLocaleString()}
                />
                <Tooltip />
                <Bar dataKey='amount' fill='#8884d8' />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      )}

      {/* Commitments Breakdown Bar Chart */}
      {selectedInvestor && filteredCommitments.length > 0 && (
        <Card className='mt-6'>
          <CardContent>
            <h2 className='text-xl font-semibold mb-4'>
              {selectedAssetClass
                ? `Commitments Breakdown (${selectedAssetClass})`
                : 'Commitments Breakdown'}
            </h2>
            <ResponsiveContainer width='100%' height={300}>
              <BarChart data={filteredCommitments}>
                <XAxis dataKey='asset_class' />
                <YAxis
                  width={90} // Ensure space for Y-axis labels
                  tickFormatter={(value) => value.toLocaleString()}
                />
                <Tooltip />
                <Bar dataKey='amount' fill='#8884d8' />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      )}

      {/* Commitments Grouped by Asset Class */}
      {selectedInvestor && groupedData.length > 0 && (
        <Card className='mt-6'>
          <CardContent>
            <h2 className='text-xl font-semibold mb-4'>
              Commitments Grouped by Asset Class
            </h2>
            <ResponsiveContainer width='100%' height={300}>
              <BarChart data={groupedData}>
                <XAxis dataKey='asset_class' />
                <YAxis
                  width={90} // Ensure space for Y-axis labels
                  tickFormatter={(value) => value.toLocaleString()}
                />
                <Tooltip />
                <Bar dataKey='amount' fill='#82ca9d' />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
