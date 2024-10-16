import { create } from "zustand";

export const useModelDataStore = create((set, get) => ({
  dataForm: undefined,
  setDataForm: (newDataForm) => set({ dataForm: newDataForm }),
  resetDataForm: () => set({ dataForm: undefined }),
}));
