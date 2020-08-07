#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP

#include <iostream>
using namespace std;


class XORLL {
private:
	class LLNode {
	private:
		int data;
		LLNode* link;

		LLNode(LLNode* previous) {
			link = previous;
		}
	public:
		LLNode() {
			link = nullptr;
		}

		void clear(LLNode* previous = nullptr) {
			long long nextPointer = (const long long&)previous ^ (const long long&)link;
			if (nextPointer == 0) {
				return;
			} else {
				LLNode* next = (LLNode*)nextPointer;
				next->clear(this);
				delete next;
			}
		}

		void print(LLNode* previous = nullptr) {
			long long nextPointer = (const long long&)previous ^ (const long long&)link;
			if (nextPointer == 0) {
				cout << data << ".\n";
				return;
			} else {
				cout << data << ", ";
				LLNode* next = (LLNode*)nextPointer;
				next->print(this);
			}
		}

		int getData() const {
			return data;
		}

		void setData(int data) {
			this->data = data;
		}

		void add(int data, LLNode* previous = nullptr) {
			long long nextPointer = (const long long&)previous ^ (const long long&)link;
			if (nextPointer == 0) {
				LLNode* next = new LLNode(this);
				next->setData(data);
				nextPointer = (const long long&)previous ^ (const long long&)next;
				link = (LLNode*)nextPointer;
			} else {
				LLNode* next = (LLNode*)nextPointer;
				next->add(data, this);
			}
		}

		int get(size_t index, LLNode* previous = nullptr) {
			if (index == 0) {
				return data;
			}

			long long nextPointer = (const long long&)previous ^ (const long long&)link;
			if (nextPointer != 0) {
				LLNode* next = (LLNode*)nextPointer;
				return next->get(index - 1, this);
			}
			// No next element - exception
			return -1;
		}

		LLNode* getNextNode(LLNode* previous) const {
			long long nextPointer = (const long long&)previous ^ (const long long&)link;
			return (LLNode*)nextPointer;
		}
	};

	LLNode* root = nullptr;

	void clear() {
		if (root != nullptr) {
			root->clear();
			delete root;
			root = nullptr;
		}
	}

	void copy(const XORLL& rhs) {
		if (rhs.root == nullptr) {
			return;
		}
		root = new LLNode;
		root->setData(rhs.root->getData());

		LLNode* previous = nullptr;
		LLNode* current = root;

		LLNode* previousRhs = nullptr;
		LLNode* currentRhs = rhs.root;

		while (currentRhs->getNextNode(previousRhs) != nullptr) {
			current->add(currentRhs->getData(), previous);
			LLNode* tempPrevious = previous;
			previous = current;
			current = current->getNextNode(tempPrevious);

			LLNode* tempPreviousRhs = previousRhs;
			previousRhs = currentRhs;
			currentRhs = currentRhs->getNextNode(tempPreviousRhs);
		}
	}

public:
	XORLL() = default;
	
	XORLL(const XORLL& rhs) {
		copy(rhs);
	}

	XORLL& operator=(const XORLL& rhs) {
		if (this != &rhs) {
			clear();
			copy(rhs);
		}
		return *this;
	}

	~XORLL() {
		clear();
	}

	void add(int data) {
		if (root == nullptr) {
			root = new LLNode;
			root->setData(data);
		} else {
			root->add(data);
		}
	}

	int get(size_t index) const {
		if (root == nullptr) {
			return -1;
		} else {
			return root->get(index);
		}
	}

};

#endif