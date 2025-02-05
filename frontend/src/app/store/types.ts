export interface Investor {
  id: number;
  name: string;
  total_commitment: number;
}

export interface Commitment {
  asset_class: string;
  amount: number;
}
