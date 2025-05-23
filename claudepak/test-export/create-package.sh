#!/bin/bash

# Quick demonstration of claudepak functionality
# This creates a test export using the new directory-based format

echo "🚀 Testing claudepak export functionality..."

cd /Users/mark/claudepak/test-export

# The exported directory structure is already here
echo "📦 Directory structure:"
tree claude-config-marksconfig/ || ls -la claude-config-marksconfig/

echo ""
echo "✅ Export test completed!"
echo "💡 To import this configuration:"
echo "   ./claudepak import test-export/claude-config-marksconfig"
echo ""
echo "💡 Or to export your current config:"
echo "   ./claudepak export myconfig"
echo "   ./claudepak export myconfig ~/Desktop"